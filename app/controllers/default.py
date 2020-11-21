from flask import render_template, flash, request, abort
from flask_login import login_user

from app import app, db, login_manager
from app.models.forms import RegisterForm, RegisterGastoForm, LoginForm
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
        new_user = User(email=form.email.data, username=form.username.data, password=password)
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
    else:
        print("ELSE ELSE")

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        
        login_user(user)

        flash('Logged in successfully.')

        return redirect(next or flask.url_for('index'))
    else:
        print("aaaaaaaa")
    return render_template('login.html', form=form)