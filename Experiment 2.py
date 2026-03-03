import pandas as pd

data = {
    'Customer_ID': [101, 102, 101, 103, 102, 101],
    'Order_Date': ['2026-01-10', '2026-01-12', '2026-01-15',
                   '2026-01-18', '2026-01-20', '2026-01-25'],
    'Product_Name': ['Laptop', 'Mobile', 'Tablet',
                     'Laptop', 'Tablet', 'Mobile'],
    'Order_Quantity': [1, 2, 1, 3, 2, 1]
}

order_data = pd.DataFrame(data)

order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

orders_per_customer = order_data.groupby('Customer_ID').size()

avg_quantity_per_product = order_data.groupby('Product_Name')['Order_Quantity'].mean()

earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

print("Total Orders per Customer:\n", orders_per_customer)
print("\nAverage Quantity per Product:\n", avg_quantity_per_product)
print("\nEarliest Order Date:", earliest_date)
print("Latest Order Date:", latest_date)
