from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, Float


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Gasto(db.Model):
    __tablename__ = "gastos"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, ForeignKey('users.id'))
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    produto = db.Column(db.Text)
    mes = db.Column(db.Integer)

    def __init__(self, id_user, valor, data, produto, mes):
        self.id_user = id_user
        self.valor = valor
        self.data = data
        self.produto = produto
        self.mes = mes

    def __repr__(self):
        if self.produto:
            return '<Gasto %r>' % self.produto

        return '<Gasto %r>' % self.id