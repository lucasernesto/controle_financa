from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length, DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=5, max=10, message='Must be between 5 and 10 characters')])
    password = PasswordField("password", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
