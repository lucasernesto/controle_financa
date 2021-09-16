from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    validators,
    FloatField,
    DateTimeField,
    IntegerField,
    DateField,
    BooleanField,
)
from wtforms.fields.core import BooleanField
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
    # TODO Corrigir erro de não conseguir pegar float no campo valor

    nome = StringField("nome")
    valor = FloatField("valor", validators=[InputRequired()])
    tipo = StringField("tipo")
    date = DateField("data", format="%d/%m/%Y")
    dia_vencimento = StringField("dia_vencimento")
    conta_a_pagar = StringField("conta_a_pagar")
    mes = IntegerField("mes")
    ano = IntegerField("ano")
    pago = BooleanField("pago")
    meses_a_ficar = IntegerField("meses_a_ficar")
