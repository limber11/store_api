import pytest  # Importación del módulo pytest para escribir pruebas unitarias
from flask_jwt_extended import create_access_token  # Importación de la función create_access_token de Flask-JWT-Extended

from app.database import db  # Importación del objeto db desde el módulo database de la aplicación
from app.run import app  # Importación de la aplicación Flask desde el módulo run de la aplicación

# Fixture para configurar un cliente de prueba
@pytest.fixture(scope="module")
def test_client():
    # Configuración de la aplicación Flask para el entorno de pruebas
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # Configuración de una base de datos en memoria para las pruebas
    app.config["JWT_SECRET_KEY"] = "test_secret_key"  # Configuración de la clave secreta para JWT

    # Creación del cliente de prueba
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()  # Creación de las tablas en la base de datos de prueba
            yield testing_client  # Provee el cliente de prueba para las pruebas
            db.drop_all()  # Eliminación de las tablas de la base de datos de prueba al finalizar las pruebas

# Fixture para generar headers de autorización de administrador
@pytest.fixture(scope="module")
def admin_auth_headers():
    with app.app_context():
        # Creación de un token de acceso para un usuario administrador
        access_token = create_access_token(
            identity={"username": "testuser", "roles": '["admin"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}  # Creación de los headers de autorización
        return headers

# Fixture para generar headers de autorización de usuario regular
@pytest.fixture(scope="module")
def user_auth_headers():
    with app.app_context():
        # Creación de un token de acceso para un usuario regular
        access_token = create_access_token(
            identity={"username": "user", "roles": '["user"]'}
        )
        headers = {"Authorization": f"Bearer {access_token}"}  # Creación de los headers de autorización
        return headers
