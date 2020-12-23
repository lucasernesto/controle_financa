# do modulo tal import a classe tal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
# passando arquivos de config atraves de um arquivo sem sua extensao
app.config.from_object('config')
# recebe a instancia do flask definida acima
db = SQLAlchemy(app)
login_manager = LoginManager()


# python3 import completo do modulo, nao pode ser relativo
from app.models import tables, forms
from app.controllers import default