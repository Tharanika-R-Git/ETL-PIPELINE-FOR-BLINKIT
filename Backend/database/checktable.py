import sqlite3

# Connect to the same DB
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

# Check all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())  # Expected output: [('products',)]

conn.close()