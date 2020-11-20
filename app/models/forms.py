from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, FloatField, DateTimeField, IntegerField
from wtforms.validators import InputRequired, Email, Length, DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(), Length(min=5, max=10, message='Must be between 5 and 10 characters')])
    password = PasswordField("password", validators=[InputRequired()])

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class RegisterGastoForm(FlaskForm):
    valor = FloatField('valor', validators=[InputRequired()])
    data = DateTimeField('data', format='%m/%d/%y', validators=[InputRequired()])
    produto = StringField('produto')
    mes = IntegerField('mes')