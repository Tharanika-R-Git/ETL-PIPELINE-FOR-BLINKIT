import sqlite3

conn = sqlite3.connect("../database/products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection TEXT,
    product_name TEXT,
    category TEXT,
    sub_category TEXT,
    price REAL,
    rating REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()