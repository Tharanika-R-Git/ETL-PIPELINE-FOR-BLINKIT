# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from typing import List, Optional
from pydantic import BaseModel
import os

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI(title="Blinkit Products API")

# Allow frontend (React) to access APIs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change to your frontend URL in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Root route to avoid 404
# -----------------------------
@app.get("/")
def root():
    return {"message": "Blinkit Products API is running!"}

# -----------------------------
# Pydantic model for Product
# -----------------------------
class Product(BaseModel):
    id: int
    collection: Optional[str] = None
    product_name: str
    category: Optional[str] = None
    sub_category: str
    price: Optional[float] = None
    rating: Optional[float] = None
    timestamp: Optional[str] = None
# -----------------------------
# Database path
# -----------------------------
DB_PATH = os.path.join(os.path.dirname(__file__), "database", "products.db")

# Optional: check if DB exists
if not os.path.exists(DB_PATH):
    raise FileNotFoundError(f"Database file not found at: {DB_PATH}")
# -----------------------------
# Helper function to query DB
# -----------------------------
def query_db(query: str, params=()):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# -----------------------------
# API Endpoints
# -----------------------------

# Get all products (limit optional)
@app.get("/products", response_model=List[Product])
def get_products(limit: int = 100):
    query = "SELECT * FROM products LIMIT ?"
    return query_db(query, (limit,))

# Get product by ID
@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    query = "SELECT * FROM products WHERE id = ?"
    results = query_db(query, (product_id,))
    if not results:
        raise HTTPException(status_code=404, detail="Product not found")
    return results[0]

# Get unique categories
@app.get("/categories")
def get_categories():
    query = "SELECT DISTINCT category FROM products"
    categories = query_db(query)
    return [c["category"] for c in categories]

# Get top N products by price
@app.get("/products/top")
def get_top_products(limit: int = 10):
    query = "SELECT * FROM products ORDER BY price DESC LIMIT ?"
    return query_db(query, (limit,))

# Get latest N products
@app.get("/products/latest")
def get_latest_products(limit: int = 10):
    query = "SELECT * FROM products ORDER BY timestamp DESC LIMIT ?"
    return query_db(query, (limit,))
    import os
import uvicorn

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)