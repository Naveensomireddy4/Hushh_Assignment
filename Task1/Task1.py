from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import asyncpg

# Create the FastAPI instance
app = FastAPI()

# PostgreSQL connection configuration
DATABASE_URL = "postgresql://postgres:1234@localhost:5433/hush"

# Pydantic models for request and response validation
class User(BaseModel):
    name: str
    email: str

class Order(BaseModel):
    user_id: int
    product_name: str
    quantity: int

# Database connection dependency
async def get_db():
    try:
        conn = await asyncpg.connect(DATABASE_URL)
        yield conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")
    finally:
        await conn.close()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}


@app.post("/users/")
async def create_user(user: User, db: asyncpg.Connection = Depends(get_db)):
    result = await db.fetchrow("INSERT INTO users(name, email) VALUES($1, $2) RETURNING id", user.name, user.email)
    print("user created")
    return {"id": result["id"], "name": user.name, "email": user.email}

@app.get("/users/{id}")
async def get_user(id: int, db: asyncpg.Connection = Depends(get_db)):
    user = await db.fetchrow("SELECT * FROM users WHERE id = $1", id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user["id"], "name": user["name"], "email": user["email"]}

@app.put("/users/{id}")
async def update_user(id: int, user: User, db: asyncpg.Connection = Depends(get_db)):
    await db.execute("UPDATE users SET name = $1, email = $2 WHERE id = $3", user.name, user.email, id)
    return {"id": id, "name": user.name, "email": user.email}

@app.delete("/users/{id}")
async def delete_user(id: int, db: asyncpg.Connection = Depends(get_db)):
    query = "DELETE FROM users WHERE id = $1 RETURNING id"
    result = await db.fetchrow(query, id)  # Use 'id' instead of 'user_id'
    
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"id": result["id"], "message": "User deleted successfully"}


# CRUD operations for orders can be added similarly


@app.post("/orders/")
async def create_order(order: Order, db: asyncpg.Connection = Depends(get_db)):
    result = await db.fetchrow("INSERT INTO orders(user_id, product_name, quantity) VALUES($1, $2, $3) RETURNING id", order.user_id, order.product_name, order.quantity)
    return {"id": result["id"], "user_id": order.user_id, "product_name": order.product_name, "quantity": order.quantity}

@app.get("/orders/{id}")
async def get_order(id: int, db: asyncpg.Connection = Depends(get_db)):
    order = await db.fetchrow("SELECT * FROM orders WHERE id = $1", id)
    if order is None:
        raise HTTPException(status_code=404, detail="order not found")
    return {"id": order["id"],  "user_id": order["user_id"], "product_name": order["product_name"], "quantity": order["quantity"]}

@app.put("/orders/{id}")
async def update_order(id: int, order: Order, db: asyncpg.Connection = Depends(get_db)):
    await db.execute("UPDATE orders SET product_name = $1, quantity = $2 WHERE id = $3", order.product_name, order.quantity, id)
    return {"id": id, "product_name": order.product_name, "quantity": order.quantity}

@app.delete("/orders/{id}")
async def delete_order(id: int, db: asyncpg.Connection = Depends(get_db)):
    result = await db.fetchrow("DELETE FROM orders WHERE id = $1 RETURNING id", id)
    if result is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": result["id"], "message": "Order deleted successfully"}

# # CRUD operations for orders can be added similarly

