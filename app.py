from flask import Flask, render_template
from forms.forms import *

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisisasecretkey'

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route("/form", methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate():
        return 'The form has beem submit'
    return render_template('form.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    #TODO Corrigir erro no validate da Form
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user has been created!</h1>'
    else:
        print("asdasda")

    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)