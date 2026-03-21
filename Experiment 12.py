import pandas as pd

# Creating dataset
data = {
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones',
                'Keyboard', 'Mouse', 'Smartwatch', 'Camera'],
    'Quantity_Sold': [50, 120, 70, 90, 60, 80, 40, 30]
}

# Creating DataFrame
sales_data = pd.DataFrame(data)

# Finding top 5 most sold products
top_products = sales_data.sort_values(by='Quantity_Sold', ascending=False).head(5)

print("Top 5 Most Sold Products:")
print(top_products)
