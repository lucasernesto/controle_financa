from flask import render_template

from app import app, db
from app.models.forms import RegisterForm
from app.models.tables import User
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