from flask import render_template

from app import app, db
from app.models.forms import RegisterForm, RegisterGastoForm
from app.models.tables import User, Gasto
from passlib.hash import sha256_crypt

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        password = sha256_crypt.encrypt(form.password.data)
        new_user = User(form.email.data, form.username.data, password)
        db.session.add(new_user)
        db.session.commit()

    return render_template('signup.html', form=form)


@app.route('/gasto', methods=['GET', 'POST'])
def gasto():
    form = RegisterGastoForm()

    if form.validate_on_submit():
        data = form.data.data
        new_gasto = Gasto(form.valor.data, form.data.data, form.produto.data)
        db.session.add(new_gasto)
        db.session.commit()
    else:
        print("aaaa")

    return render_template('gasto.html', form=form)
