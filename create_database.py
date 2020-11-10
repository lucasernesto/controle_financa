from app import db, app

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.create_all()

print("------------------------------------------")
print("B A N C O   D E   D A D O S   C R I A D O")
print("------------------------------------------")
