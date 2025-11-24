import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# 2. Write SQL query to get total quantity and revenue per product
query = """
SELECT 
    product,
    SUM(quantity) AS total_qty,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# 3. Load SQL result into pandas DataFrame
df = pd.read_sql_query(query, conn)

# 4. Print the summary table
print("=== Sales Summary ===")
print(df)

# 5. Plot bar chart of revenue by product
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product')
plt.ylabel("Revenue")
plt.tight_layout()

# 6. Save chart (optional) and show
plt.savefig("sales_chart.png")
plt.show()

# 7. Close the connection
conn.close()
