# do modulo tal import a classe tal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

db = SQLAlchemy(app)
    

@login_manager.user_loader
def load_user(user_id):
    return tables.User.query.filter_by(id=user_id).first()

# python3 import completo do modulo, nao pode ser relativo
from app.models import tables, forms
from app.controllers import default