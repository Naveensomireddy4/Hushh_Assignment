import pytest
from fastapi.testclient import TestClient
from Task1 import app  # Import the FastAPI app from your main.py file

# # To run the tests, you can use pytest from the terminal:
# # pytest test.py
client = TestClient(app)



def test_create_user():
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]

# Test case for fetching a user by ID (GET /users/{id})
def test_get_user():
    user_data = {"name": "Alice", "email": "alice@example.com"}
    create_response = client.post("/users/", json=user_data)
    user_id = create_response.json()["id"]
    
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]
    assert data["email"] == user_data["email"]

# Test case for updating user information (PUT /users/{id})
def test_update_user():
    user_data = {"name": "Bob", "email": "bob@gmail.com"}
    create_response = client.post("/users/", json=user_data)
    assert create_response.status_code == 200 # Check if user creation is successful
    user_id = create_response.json()["id"]

    updated_data = {"name": "Robert", "email": "robert@gmail.com"}
    response = client.put(f"/users/{user_id}", json=updated_data)
    
    # Debugging output
    print(response.status_code)
    print(response.text)  # This will help you see the full response from the server
    
    data = response.json()
    assert response.status_code == 200

    assert data["id"] == user_id
    assert data["name"] == updated_data["name"]
    assert data["email"] == updated_data["email"]


import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_delete_user():
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Create a user
        user_data = {"name": "Charlie", "email": "charlie@example.com"}
        create_response = await client.post("/users/", json=user_data)
        assert create_response.status_code == 200  # Assuming successful creation returns 201
        
        user_id = create_response.json()["id"]
        print(f"Created user ID: {user_id}")

        # Delete the user
        delete_response = await client.delete(f"/users/{user_id}")
        assert delete_response.status_code == 200
        
        data = delete_response.json()
        assert data["id"] == user_id
        assert data["message"] == "User deleted successfully"

        # Try fetching the deleted user
        fetch_response = await client.get(f"/users/{user_id}")
        assert fetch_response.status_code == 500  # User should be deleted


# Test case for creating an order (POST /orders/)
def test_create_order():
    user_data = {"name": "David", "email": "david@example.com"}
    create_user_response = client.post("/users/", json=user_data)
    user_id = create_user_response.json()["id"]
    
    order_data = {"user_id": user_id, "product_name": "Laptop", "quantity": 2}
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["user_id"] == user_id
    assert data["product_name"] == order_data["product_name"]
    assert data["quantity"] == order_data["quantity"]

# Test case for fetching an order by ID (GET /orders/{id})
def test_get_order():
    user_data = {"name": "Eve", "email": "eve@example.com"}
    create_user_response = client.post("/users/", json=user_data)
    user_id = create_user_response.json()["id"]
    
    order_data = {"user_id": user_id, "product_name": "Smartphone", "quantity": 1}
    create_order_response = client.post("/orders/", json=order_data)
    order_id = create_order_response.json()["id"]
    
    response = client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["user_id"] == user_id
    assert data["product_name"] == order_data["product_name"]
    assert data["quantity"] == order_data["quantity"]


def test_update_order():
    user_data = {"name": "Frank", "email": "frank@example.com"}
    create_user_response = client.post("/users/", json=user_data)
    user_id = create_user_response.json()["id"]
    
    order_data = {"user_id": user_id, "product_name": "Tablet", "quantity": 3}
    create_order_response = client.post("/orders/", json=order_data)
    order_id = create_order_response.json()["id"]
 

    
    updated_order_data = {"user_id": user_id,"product_name": "Smartwatch", "quantity": 5}
    response = client.put(f"/orders/{order_id}", json=updated_order_data)
    print(response.status_code)
    print(response.json())  # Print the detailed
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["product_name"] == updated_order_data["product_name"]
    assert data["quantity"] == updated_order_data["quantity"]

# Test case for deleting an order (DELETE /orders/{id})
def test_delete_order():
    user_data = {"name": "Grace", "email": "grace@example.com"}
    create_user_response = client.post("/users/", json=user_data)
    user_id = create_user_response.json()["id"]
    
    order_data = {"user_id": user_id, "product_name": "Headphones", "quantity": 1}
    create_order_response = client.post("/orders/", json=order_data)
    order_id = create_order_response.json()["id"]
    
    response = client.delete(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id
    assert data["message"] == "Order deleted successfully"
    
    fetch_response = client.get(f"/orders/{order_id}")
    assert fetch_response.status_code == 500  # Order should be deleted



