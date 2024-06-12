import json  # Importación del módulo json para trabajar con datos JSON
from flask_login import UserMixin  # Importación de la clase UserMixin de Flask-Login para facilitar la implementación de usuarios
from werkzeug.security import check_password_hash, generate_password_hash  # Importación de funciones para hash de contraseñas

from app.database import db  # Importación del objeto db desde el módulo database de la aplicación

# Definición de la clase User
class User(UserMixin, db.Model):
    # Configuración de la tabla de la base de datos
    __tablename__ = "users"

    # Definición de columnas
    id = db.Column(db.Integer, primary_key=True)  # Clave primaria de tipo entero
    username = db.Column(db.String(50), unique=True, nullable=False)  # Nombre de usuario (cadena de máximo 50 caracteres, único y no nulo)
    password_hash = db.Column(db.String(128), nullable=False)  # Hash de la contraseña (cadena de máximo 128 caracteres, no nulo)
    roles = db.Column(db.String(50), nullable=False)  # Roles del usuario (cadena de máximo 50 caracteres, no nulo)

    # Constructor
    def __init__(self, username, password, roles=["user"]):
        self.username = username
        self.roles = json.dumps(roles)  # Convierte la lista de roles a formato JSON antes de almacenarla
        self.password_hash = generate_password_hash(password)  # Genera el hash de la contraseña antes de almacenarla

    # Método para guardar el usuario en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Método estático para buscar un usuario por su nombre de usuario
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()
