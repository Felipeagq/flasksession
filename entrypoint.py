from flask import Flask, json, jsonify, session, escape
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
import os 

# Configuraciones
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["TRACK_MODIFICATIONS"] =  True
db = SQLAlchemy(app)
app.config["SECRET_KEY"] = "camila"


# Creación del modelo para database.db
class User(db.Model):
    __tablename__ = "USERS"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Archivo .db
if os.path.exists("database.db"):
    db.create_all()
else:
    print("database already exists")


# RUTA INDEX
@app.route("/")
def index():
    return jsonify({"msg":"ok","route":"index"})

# CREACION DE USUARIOS
@app.route("/signup")
def signup():
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    hashed_pw = generate_password_hash(password,method="sha256")
    print(hashed_pw)
    user = User(username=username, password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return f"{username} have been load correctly"

# LISTADO DE USUARIOS
@app.route("/all")
def all():
    user = User.query.all()
    usuarios = []
    for usuario in user:
        usuarios.append(usuario.username)
    return jsonify({"msg":"ok",
    "data":usuarios})


# LOGGEO DE SESIÓN
@app.route("/login")
def login():
    user = input("ingrese usuario: ")
    password = input("ingrese contraseña: ")

    usuario = User.query.filter_by(username=user).first()

    if usuario and check_password_hash(usuario.password, password):
        print("bien")
        session["username"] = user
        return jsonify({"msg":"ok",
        "data":"you logged good"})
    return jsonify({"msg":"ok",
    "data":"bad credentials"})


# COMPROBACIÓN DE LOGGEO
@app.route("/home")
def home():
    if "username" in session:
        return f"You are {escape(session['username'])}"
    return "you are not logged"


# DESLOGGEO
@app.route("/logout")
def logout():
    session.pop("username",None)
    return "You have been logged out"


# MANEJADOR DE ERRORES
@app.errorhandler(Exception)
def error(e):
    return jsonify({"error":f"{e}"})



if __name__ == "__main__":
    app.run(debug=True)