import os
import sqlite3
import pandas as pd

# -----------------------------
# Step 1: Set paths
# -----------------------------
# Project root folder (one level up from this script)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Path to processed CSV
csv_path = os.path.join(project_root, "data", "processed", "clean_productsnew.csv")
print("Loading CSV:", csv_path)

# Path to SQLite DB
db_path = os.path.join(project_root, "database", "products.db")

# -----------------------------
# Step 2: Load CSV
# -----------------------------
df = pd.read_csv(csv_path)
print(f"CSV loaded. Number of rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")

# -----------------------------
# Step 3: Connect to SQLite
# -----------------------------
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# -----------------------------
# Step 4: Create table if not exists
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    collection TEXT,
    product_name TEXT,
    category TEXT,
    sub_category TEXT,
    price REAL,
    rating REAL,
    timestamp DATETIME
)
""")

# -----------------------------
# Step 5: Insert CSV rows into SQLite
# -----------------------------
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO products (collection, product_name, category, sub_category, price, rating, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        row.get("brand", ""),             # collection
        row.get("name", ""),              # product_name
        row.get("category", ""),          # category
        "",                               # sub_category (empty for now)
        row.get("selling_price", None),   # price
        None,                             # rating (not in CSV)
        row.get("ingestion_time", None)   # timestamp
    ))

# -----------------------------
# Step 6: Commit and close DB
# -----------------------------
conn.commit()
conn.close()
print("CSV data loaded into products.db successfully!")