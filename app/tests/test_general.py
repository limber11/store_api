# Definición de una función de prueba para la ruta principal
def test_index(test_client):
    # Realiza una solicitud GET a la ruta principal "/"
    response = test_client.get("/")
    # Verifica que el código de estado de la respuesta sea 404 (No Encontrado)
    assert response.status_code == 404

# Definición de una función de prueba para la interfaz de usuario de Swagger
def test_swagger_ui(test_client):
    # Realiza una solicitud GET a la ruta "/api/docs/"
    response = test_client.get("/api/docs/")
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que el contenido de la respuesta contenga el identificador "swagger-ui"
    assert b'id="swagger-ui"' in response.data
