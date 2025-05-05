import pandas as pd

# Load the sales data
sales_data = pd.read_csv('task\\sales_data.csv')

# 1. Group the data by 'Category' and calculate aggregate statistics
category_group = sales_data.groupby('Category').agg(
    total_quantity_sold=('Quantity', 'sum'),
    avg_price_per_unit=('Price', 'mean'),
    max_quantity_sold=('Quantity', 'max')
).reset_index()

print("Aggregated data by Category:")
print(category_group)

# 2. Identify the top-selling product in each category
top_selling_product = sales_data.groupby(['Category', 'Product']).agg(
    total_quantity_sold=('Quantity', 'sum')
).reset_index()

top_selling_product = top_selling_product.loc[top_selling_product.groupby('Category')['total_quantity_sold'].idxmax()]
print("\nTop-selling product in each category:")
print(top_selling_product)

# 3. Find the date on which the highest total sales (quantity * price) occurred
sales_data['total_sales'] = sales_data['Quantity'] * sales_data['Price']
max_sales_date = sales_data.groupby('Date')['total_sales'].sum().idxmax()
print("\nDate with the highest total sales:")
print(max_sales_date)
