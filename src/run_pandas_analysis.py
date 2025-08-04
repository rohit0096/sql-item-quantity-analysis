import pandas as pd
from db_connect import get_connection

conn= get_connection()
# Load tables
customers = pd.read_sql("SELECT * FROM Customer", conn)
orders = pd.read_sql("SELECT * FROM Orders", conn)
sales = pd.read_sql("SELECT * FROM Sales", conn)
items = pd.read_sql("SELECT * FROM Items", conn)


# Step 1: Merge Customer with Sales
merged_df = pd.merge(customers, sales, on="customer_id")

# Step 2: Merge with Orders on sales_id
merged_df = pd.merge(merged_df, orders, on="sales_id")

# Step 3: Merge with Items on item_id
merged_df = pd.merge(merged_df, items, on="item_id")


# Step 4: Filter customers aged between 18 and 35
filtered_df = merged_df[(merged_df["age"] >= 18) & (merged_df["age"] <= 35)]

# Step 5: Group by customer_id, age, item_name and sum quantity
grouped_df = (
    filtered_df.groupby(["customer_id", "age", "item_name"])["quantity"]
    .sum()
    .reset_index(name="Quantity")
)

# Step 6: Filter out 0 quantity
final_df = grouped_df[grouped_df["Quantity"] > 0]

# Step 7: Sort by customer_id and item_name
final_df = final_df.sort_values(by=["customer_id", "item_name"])

# Step 8: Rename columns for CSV output
final_df.rename(
    columns={
        "customer_id": "Customer",
        "age": "Age",
        "item_name": "Item"
    },
    inplace=True
)
# Step 9: Save to CSV
final_df.to_csv("src/customer_item_quantities.csv", sep=";", index=False)

print("CSV saved as 'customer_item_quantities.csv'")

conn.close()


