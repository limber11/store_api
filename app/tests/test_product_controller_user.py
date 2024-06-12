# Prueba para obtener todos los productos como un usuario regular
def test_get_products_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/productos", headers=user_auth_headers)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que la respuesta sea una lista vacía (sin productos)
    assert response.json == []

# Prueba para crear un producto como un administrador
def test_create_product(test_client, admin_auth_headers):
    data = {
        "name": "Iphone",
        "description": "el mejor iphone que vas a conseguir en to veda choqueto",
        "price": 599.99,
        "stock": 100,
    }
    response = test_client.post("/api/productos", json=data, headers=admin_auth_headers)
    # Verifica que el código de estado de la respuesta sea 201 (Creado)
    assert response.status_code == 201
    # Verifica que los datos del producto en la respuesta sean correctos
    assert response.json["name"] == "Iphone"
    assert response.json["description"] == "el mejor iphone que vas a conseguir en to veda choqueto"
    assert response.json["price"] == 599.99
    assert response.json["stock"] == 100

# Prueba para obtener un producto como un usuario regular
def test_get_product_as_user(test_client, user_auth_headers):
    response = test_client.get("/api/productos/1", headers=user_auth_headers)
    # Verifica que el código de estado de la respuesta sea 200 (OK)
    assert response.status_code == 200
    # Verifica que la respuesta contenga los campos "name", "description", "price" y "stock"
    assert "name" in response.json
    assert "description" in response.json
    assert "price" in response.json
    assert "stock" in response.json
    
# Prueba para crear un producto como un usuario regular
def test_create_product_as_user(test_client, user_auth_headers):
    data = {"name": "Laptop", "description": "High-end gaming laptop", "price": 1500.0, "stock": 10}
    response = test_client.post("/api/productos", json=data, headers=user_auth_headers)
    # Verifica que el código de estado de la respuesta sea 403 (Prohibido)
    assert response.status_code == 403

# Prueba para actualizar un producto como un usuario regular
def test_update_product_as_user(test_client, user_auth_headers):
    data = {"name": "Laptop", "description": "Updated description", "price": 1600.0, "stock": 5}
    response = test_client.put("/api/productos/1", json=data, headers=user_auth_headers)
    # Verifica que el código de estado de la respuesta sea 403 (Prohibido)
    assert response.status_code == 403

# Prueba para eliminar un producto como un usuario regular
def test_delete_product_as_user(test_client, user_auth_headers):
    response = test_client.delete("/api/productos/1", headers=user_auth_headers)
    # Verifica que el código de estado de la respuesta sea 403 (Prohibido)
    assert response.status_code == 403
