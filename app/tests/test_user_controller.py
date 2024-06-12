import pytest  # Importación del módulo pytest para escribir pruebas unitarias
from app.models.user_model import User  # Importación del modelo User desde el módulo user_model de la aplicación

# Fixture para crear un nuevo usuario para pruebas
@pytest.fixture
def new_user():
    return {"username": "testuser", "password": "testpassword"}

# Prueba para registrar un nuevo usuario
def test_register_user(test_client, new_user):
    response = test_client.post("/api/register", json=new_user)
    # Verifica que el código de estado de la respuesta sea 201 (Creado)
    assert response.status_code == 201
    # Verifica que la respuesta contenga el mensaje de éxito
    assert response.json["message"] == "Usuario creado exitosamente"

# Prueba para registrar un usuario duplicado
def test_register_duplicate_user(test_client, new_user):
    # Registro inicial del usuario
    test_client.post("/api/register", json=new_user)
    
    # Intento de registro del mismo usuario nuevamente
    response = test_client.post("/api/register", json=new_user)
    # Verifica que el código de estado de la respuesta sea 400 (Solicitud Incorrecta)
    assert response.status_code == 400
    # Verifica que la respuesta contenga el mensaje de error de usuario duplicado
    assert response.json["error"] == "El nombre de usuario ya está en uso"

# Prueba para iniciar sesión con un usuario registrado
def test_login_user(test_client, new_user):
    login_credentials = {
        "username": new_user["username"],
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que la respuesta contenga un token de acceso
    assert response.json["access_token"]

# Prueba para iniciar sesión con un nombre de usuario inexistente
def test_login_invalid_user(test_client, new_user):
    login_credentials = {
        "username": "nousername",
        "password": new_user["password"],
    }
    response = test_client.post("/api/login", json=login_credentials)
    # Verifica que el código de estado de la respuesta sea 401 (No autorizado)
    assert response.status_code == 401
    # Verifica que la respuesta contenga el mensaje de error de credenciales inválidas
    assert response.json["error"] == "Credenciales inválidas"

# Prueba para iniciar sesión con una contraseña incorrecta
def test_login_wrong_password(test_client, new_user):
    login_credentials = {"username": new_user["username"], "password": "wrongpassword"}
    response = test_client.post("/api/login", json=login_credentials)
    # Verifica que el código de estado de la respuesta sea 401 (No autorizado)
    assert response.status_code == 401
    # Verifica que la respuesta contenga el mensaje de error de credenciales inválidas
    assert response.json["error"] == "Credenciales inválidas"
