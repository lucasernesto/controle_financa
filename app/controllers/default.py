import pendulum
from pendulum.parsing.exceptions import ParserError

from flask import render_template, flash, request, abort, redirect
from flask_login import login_user

from app import app, db, login_manager
from app.models.forms import RegisterForm, RegisterGastoForm, LoginForm
from app.models.tables import User, Gasto
from passlib.hash import sha256_crypt


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        password = sha256_crypt.encrypt(form.password.data)
        new_user = User(
            email=form.email.data, username=form.username.data, password=password
        )
        db.session.add(new_user)
        db.session.commit()

    return render_template("signup.html", form=form)


@app.route("/gasto", methods=["GET", "POST"])
def gasto():
    form = RegisterGastoForm()
    try:
        x = pendulum.parse(str(form.date.data))
    except ParserError:
        ...
    #TODO Corrigir erro de não conseguir pegar float no campo valor
    if form.validate_on_submit():
        mes = pendulum.parse(str(form.date.data)).month
        new_gasto = Gasto(id_user=1, valor=form.valor.data, data=form.date.data, produto=form.produto.data, mes=mes)
        db.session.add(new_gasto)
        db.session.commit()

    return render_template("gasto.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            login_user(user)
            flash("Logged in successfully.")
            return redirect(next or flask.url_for("index"))


    return render_template("login.html", form=form)
