from flask import Flask, render_template, request

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

from models.forms import *
from models.tables import User

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate():
        return 'The form has beem submit'
    return render_template('form.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(form.email.data, form.username.data, form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return "PODE IR DORMIR"

    return render_template('signup.html', form=form)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)