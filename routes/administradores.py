from flask import Blueprint, request
from models.administrador import Lista
from utils.db import db


administradores = Blueprint("administradores", __name__)

@administradores.route("/administradores")
def index():

    return "Lista index"


@administradores.route("/registroadmin", methods=["POST"])
def add_admin():
    from app import create_database
    username = request.form["username"]
    password = request.form["password"]
    base_datos = request.form["base_datos"]

    new_administrador = Lista(username, password, base_datos)

    db.session.add(new_administrador)
    db.session.commit()

    create_database(base_datos)

    return "Admin creado con su base de datos y las tablas"


@administradores.route("/administradores")
def update():
    return "update a contact"


@administradores.route("/administradores/<id>")
def delete(id):
    return "eliminado"


@administradores.route("/about")
def about():
    return "about"
