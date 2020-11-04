from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, AnyOf


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=5, max=10, message='Must be between 5 and 10 characters')])
    password = PasswordField("password", validators=[InputRequired()], AnyOf(values['password', 'secret'])