# Hushh_Assignment

# FastAPI Application
Overview
This FastAPI application provides a RESTful API for managing users and orders. It connects to a PostgreSQL database using asyncpg for asynchronous database operations. The API supports CRUD (Create, Read, Update, Delete) operations for both users and orders.

Requirements
Python 3.7+
FastAPI
asyncpg
PostgreSQL
Setup
1. Install Dependencies
First, ensure you have Python 3.7 or higher installed. Then, install the necessary Python packages:

sh
Copy code
pip install fastapi[all] asyncpg
2. Database Configuration
Ensure you have a PostgreSQL database running. Update the DATABASE_URL in the code with your database credentials:

python
Copy code
DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"
Replace username, password, localhost, 5432, and database_name with your actual PostgreSQL database credentials.

3. Database Schema
Create the users and orders tables in your PostgreSQL database:

sql
Copy code
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL
);
4. Run the Application
Start the FastAPI application using uvicorn:

sh
Copy code
uvicorn main:app --reload
This will start the server on http://127.0.0.1:8000.

API Endpoints
Users Endpoints
Create User
URL: /users/

Method: POST

Request Body:

json
Copy code
{
    "name": "John Doe",
    "email": "johndoe@example.com"
}
Response:

json
Copy code
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
Get User
URL: /users/{id}

Method: GET

Response:

json
Copy code
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
Update User
URL: /users/{id}

Method: PUT

Request Body:

json
Copy code
{
    "name": "Jane Doe",
    "email": "janedoe@example.com"
}
Response:

json
Copy code
{
    "id": 1,
    "name": "Jane Doe",
    "email": "janedoe@example.com"
}
Delete User
URL: /users/{id}

Method: DELETE

Response:

json
Copy code
{
    "id": 1,
    "message": "User deleted successfully"
}
Orders Endpoints
Create Order
URL: /orders/

Method: POST

Request Body:

json
Copy code
{
    "user_id": 1,
    "product_name": "Laptop",
    "quantity": 2
}
Response:

json
Copy code
{
    "id": 1,
    "user_id": 1,
    "product_name": "Laptop",
    "quantity": 2
}
Get Order
URL: /orders/{id}

Method: GET

Response:

json
Copy code
{
    "id": 1,
    "user_id": 1,
    "product_name": "Laptop",
    "quantity": 2
}
Update Order
URL: /orders/{id}

Method: PUT

Request Body:

json
Copy code
{
    "product_name": "Smartphone",
    "quantity": 3
}
Response:

json
Copy code
{
    "id": 1,
    "product_name": "Smartphone",
    "quantity": 3
}
Delete Order
URL: /orders/{id}

Method: DELETE

Response:

json
Copy code
{
    "id": 1,
    "message": "Order deleted successfully"
}








# FastAPI CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built with FastAPI. The application allows you to manage users and orders. You can create, read, update, and delete users and their respective orders.

## Installation

1. **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the FastAPI application:**
    ```bash
    uvicorn Task1:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

### Users

- **Create a user:**
    ```http
    POST /users/
    ```
    Request body:
    ```json
    {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    ```

- **Get a user by ID:**
    ```http
    GET /users/{id}
    ```

- **Update a user:**
    ```http
    PUT /users/{id}
    ```
    Request body:
    ```json
    {
        "name": "John Smith",
        "email": "john.smith@example.com"
    }
    ```

- **Delete a user:**
    ```http
    DELETE /users/{id}
    ```

### Orders

- **Create an order:**
    ```http
    POST /orders/
    ```
    Request body:
    ```json
    {
        "user_id": 1,
        "product_name": "Laptop",
        "quantity": 2
    }
    ```

- **Get an order by ID:**
    ```http
    GET /orders/{id}
    ```

- **Update an order:**
    ```http
    PUT /orders/{id}
    ```
    Request body:
    ```json
    {
        "user_id": 1,
        "product_name": "Smartphone",
        "quantity": 1
    }
    ```

- **Delete an order:**
    ```http
    DELETE /orders/{id}
    ```

## Running the Tests

To run the tests, you can use `pytest`. Ensure you have `pytest` installed:
```bash
pip install pytest

