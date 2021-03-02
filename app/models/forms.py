from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    validators,
    FloatField,
    DateTimeField,
    IntegerField,
    DateField,
)
from wtforms.validators import InputRequired, Email, Length, DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField(
        "email",
        validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)],
    )
    username = StringField(
        "username", validators=[InputRequired(), Length(min=4, max=15)]
    )
    password = PasswordField(
        "password", validators=[InputRequired(), Length(min=8, max=80)]
    )


class RegisterGastoForm(FlaskForm):
    #TODO Corrigir erro de não conseguir pegar float no campo valor
    valor = FloatField("valor", validators=[InputRequired()])
    date = DateField("data", format="%d/%m/%Y", validators=[InputRequired()])
    produto = StringField("produto")
    mes = IntegerField("mes")
