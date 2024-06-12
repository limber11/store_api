import pytest  # Importación del módulo pytest para escribir pruebas unitarias

# Prueba para obtener todos los productos
def test_get_products(test_client, admin_auth_headers):
    response = test_client.get("/api/productos", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que la respuesta sea una lista vacía (sin productos)
    assert response.json == []

# Prueba para crear un producto
def test_create_product(test_client, admin_auth_headers):
    data = {
        "name": "Smartphone",
        "description": "Powerful smartphone with advanced features",
        "price": 599.99,
        "stock": 100,
    }
    response = test_client.post("/api/productos", json=data, headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 201 (Creado)
    assert response.status_code == 201
    # Verifica que los datos del producto en la respuesta sean correctos
    assert response.json["name"] == "Smartphone"
    assert response.json["description"] == "Powerful smartphone with advanced features"
    assert response.json["price"] == 599.99
    assert response.json["stock"] == 100

# Prueba para obtener un producto por su ID
def test_get_product(test_client, admin_auth_headers):
    response = test_client.get("/api/productos/1", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que la respuesta contenga el campo "name"
    assert "name" in response.json

# Prueba para obtener un producto inexistente por su ID
def test_get_nonexistent_product(test_client, admin_auth_headers):
    response = test_client.get("/api/productos/999", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 404 (No Encontrado)
    assert response.status_code == 404
    # Verifica que la respuesta contenga un mensaje de error
    assert response.json["error"] == "Producto no encontrado"

# Prueba para crear un producto con datos inválidos
def test_create_product_invalid_data(test_client, admin_auth_headers):
    data = {"name": "Laptop"}
    response = test_client.post("/api/productos", json=data, headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 400 (Solicitud Incorrecta)
    assert response.status_code == 400
    # Verifica que la respuesta contenga un mensaje de error
    assert response.json["error"] == "Faltan datos requeridos"

# Prueba para actualizar un producto existente
def test_update_product(test_client, admin_auth_headers):
    data = {
        "name": "Smartphone Pro",
        "description": "Updated version with improved performance",
        "price": 699.99,
        "stock": 150,
    }
    response = test_client.put("/api/productos/1", json=data, headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que los datos del producto en la respuesta sean correctos
    assert response.json["name"] == "Smartphone Pro"
    assert response.json["description"] == "Updated version with improved performance"
    assert response.json["price"] == 699.99
    assert response.json["stock"] == 150

# Prueba para actualizar un producto inexistente
def test_update_nonexistent_product(test_client, admin_auth_headers):
    data = {
        "name": "Tablet",
        "description": "Portable device with touchscreen interface",
        "price": 299.99,
        "stock": 50,
    }
    response = test_client.put("/api/productos/999", json=data, headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 404 (No Encontrado)
    assert response.status_code == 404
    # Verifica que la respuesta contenga un mensaje de error
    assert response.json["error"] == "Producto no encontrado"

# Prueba para eliminar un producto existente
def test_delete_product(test_client, admin_auth_headers):
    response = test_client.delete("/api/productos/1", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 204 (Sin Contenido)
    assert response.status_code == 204

    response = test_client.get("/api/productos/1", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 404 (No Encontrado)
    assert response.status_code == 404
    # Verifica que la respuesta contenga un mensaje de error
    assert response.json["error"] == "Producto no encontrado"

# Prueba para eliminar un producto inexistente
def test_delete_nonexistent_product(test_client, admin_auth_headers):
    response = test_client.delete("/api/productos/999", headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 404 (No Encontrado)
    assert response.status_code == 404
    # Verifica que la respuesta contenga un mensaje de error
    assert response.json["error"] == "Producto no encontrado"
