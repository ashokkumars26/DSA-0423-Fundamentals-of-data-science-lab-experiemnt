import pandas as pd

data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile'],
    'Price': [50000, 20000, 15000, 50000, 20000],
    'Quantity': [2, 3, 4, 1, 2]
}

sales_data = pd.DataFrame(data)

# Calculating Total Sales
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Displaying updated DataFrame
print(sales_data)
