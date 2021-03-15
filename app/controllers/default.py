import pendulum, flask
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
            new_gasto = Gasto(
                id_user=current_user.id,
                valor=format(form.valor.data, ".2g"),
                data=form.date.data,
                produto=form.produto.data,
                mes=mes,
            )
            db.session.add(new_gasto)
            db.session.commit()

    # TODO fazer pesquisar mes e aparecer os resultador que o usuario deseja
    mes = 3

    rows = Gasto.query.filter_by(id_user=current_user.id, mes=mes).all()
    total = get_total(rows)

    return render_template("home.html", form=form, rows=rows, total=total)


@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("index"))


def get_total(rows):
    total = 0
    for row in rows:
        total += row.valor

    return total
