from utils.db import db

class Lista(db.Model):
    _tablename__ = "lista"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    base_datos = db.Column(db.String(20))

    def __init__(self, username, password, base_datos):
        self.username = username
        self.password = password
        self.base_datos = base_datos
