from flask import render_template

from app import app, db
from app.models.forms import RegisterForm
from app.models.tables import User

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

    return render_template('signup.html', form=form)