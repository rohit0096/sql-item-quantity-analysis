import pandas as pd
from db_connect import get_connection

conn= get_connection()
query = """
SELECT 
    c.customer_id,
    c.age,
    i.item_name,
    o.quantity
FROM Customer c
JOIN Sales s ON c.customer_id = s.customer_id
JOIN Orders o ON s.sales_id = o.sales_id
JOIN Items i ON o.item_id = i.item_id
"""

df = pd.read_sql(query, conn)

# Filter customers aged 18-35
df_filtered = df[(df['age'] >= 18) & (df['age'] <= 35)]

# Group by customer and item, sum quantities
result = df_filtered.groupby(['customer_id', 'item_name'], as_index=False)['quantity'].sum()

# Remove entries where total quantity = 0
result = result[result['quantity'] > 0]

# Convert quantity to integer (no decimals)
result['quantity'] = result['quantity'].astype(int)

# Save to CSV with semicolon delimiter
result.to_csv(r'D:\Python\sql_item_quantity_project\src\customer_item_quantities.csv', sep=';', index=False)

print("CSV saved as 'customer_item_quantities.csv'")

