import sqlite3
import pandas as pd


conn = sqlite3.connect('chinook.db')


invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
customers = pd.read_sql_query("SELECT * FROM customers", conn)


customer_totals = invoices.groupby('CustomerId')['Total'].sum().reset_index()


customer_totals = customer_totals.merge(customers[['CustomerId', 'FirstName', 'LastName']], on='CustomerId')


top_5_customers = customer_totals.sort_values(by='Total', ascending=False).head(5)


print("Top 5 Customers with Highest Total Purchases:")
print(top_5_customers[['CustomerId', 'FirstName', 'LastName', 'Total']])


conn.close()

