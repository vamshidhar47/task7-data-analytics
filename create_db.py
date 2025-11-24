import sqlite3

# 1. Create / connect to SQLite database file
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# 2. Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# 3. Insert some sample rows
data = [
    ("Laptop", 5, 55000),
    ("Mouse", 20, 500),
    ("Keyboard", 10, 1200),
    ("Headphones", 8, 2000),
    ("Monitor", 4, 15000),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", data)

# 4. Save and close
conn.commit()
conn.close()

print("✅ sales_data.db created and sample data inserted.")
