import pendulum, flask, werkzeug
from pendulum.parsing.exceptions import ParserError

from flask import (
    render_template,
    flash,
    request,
    abort,
    redirect,
    url_for,
    abort,
    get_flashed_messages,
)
from flask_login import login_user, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError

from app import app, db, login_manager
from app.models.forms import RegisterForm, RegisterGastoForm, LoginForm
from app.models.tables import User, Gasto
from passlib.hash import sha256_crypt


@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = LoginForm()

    if request.method == "POST":
        user = User.query.filter_by(username=form.username.data).first()

        if form.validate_on_submit() and sha256_crypt.verify(
            form.password.data, user.password
        ):
            login_user(user)
            return redirect(url_for("home"))

        flash("USUARIO OU SENHA INCORRETOS")
    return render_template("index.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        password = sha256_crypt.encrypt(str(form.password.data))
        new_user = User(
            email=form.email.data, username=form.username.data, password=password
        )
        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            flash(u"Email já cadastrado", "error")

    return render_template("signup.html", form=form)


@app.route("/gasto", methods=["GET", "POST"])
@login_required
def gasto():
    form = RegisterGastoForm()
    try:
        x = pendulum.parse(str(form.date.data))
    except ParserError:
        ...

    if request.method == "POST":
        if form.validate():
            mes = pendulum.parse(str(form.date.data)).month
            new_gasto = Gasto(
                id_user=current_user.id,
                valor=form.valor.data,
                data=form.date.data,
                produto=form.produto.data,
                mes=mes,
            )
            db.session.add(new_gasto)
            db.session.commit()
    return render_template("gasto.html", form=form)


@app.route("/contafixa", methods=["GET", "POST"])
@login_required
def contafixa():
    form = RegisterGastoForm()
    data = pendulum.today()
    mes = data.month
    ano = data.year
    if request.method == "POST":
        if form.validate():
            mes = pendulum.today().month

            for x in range(0, form.meses_a_ficar.data):
                new_mensalidade = Gasto(
                    id_user=current_user.id,
                    nome=form.nome.data,
                    valor=form.valor.data,
                    tipo="conta fixa",
                    data=None,
                    dia_vencimento=form.dia_vencimento.data,
                    mes=mes,
                    ano=ano,
                    pago=False,
                )

                data = data.add(months=1)
                mes = data.month
                ano = data.year
                db.session.add(new_mensalidade)

            db.session.commit()

    rows = Gasto.query.filter_by(
        id_user=current_user.id,
        tipo="conta fixa",
        mes=pendulum.today().month,
        ano=pendulum.today().year,
    ).all()
    total = get_total(rows)

    return render_template("contafixa.html", form=form, rows=rows, total=total)


@app.route("/login", methods=["GET", "POST"])
def login():
    return redirect(url_for("index"))


@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    form = RegisterGastoForm()

    if request.method == "POST":
        if form.validate():
            mes = pendulum.parse(str(form.date.data)).month
            ano = pendulum.parse(str(form.date.data)).year
            new_gasto = Gasto(
                id_user=current_user.id,
                nome=form.nome.data,
                valor=form.valor.data,
                tipo="gasto",
                data=form.date.data,
                dia_vencimento="",
                mes=mes,
                ano=ano,
                pago=False,
            )
            db.session.add(new_gasto)
            db.session.commit()

    # TODO fazer pesquisar mes e aparecer os resultador que o usuario deseja
    mes = pendulum.today().month
    ano = pendulum.today().year
    rows = Gasto.query.filter_by(id_user=current_user.id, mes=mes, ano=ano).all()
    total = get_total(rows)

    return render_template("home.html", form=form, rows=rows, total=total)


@app.route("/<int:id>/atualizar_pago", methods=["GET", "POST"])
def atualizar_pago(id):
    gasto = Gasto.query.filter_by(id_user=current_user.id, id=id).first()

    if gasto.pago == True:
        gasto.pago = False
    else:
        gasto.pago = True

    db.session.commit()

    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("index"))


def get_total(rows):
    total = 0
    for row in rows:
        if row.pago:
            continue

        total += row.valor

    return total
