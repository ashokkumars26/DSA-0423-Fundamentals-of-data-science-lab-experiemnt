import numpy as np

# Creating NumPy array
sales_data = np.array([
    [101, 5, 500],
    [102, 3, 750],
    [103, 10, 300],
    [104, 2, 1200],
    [105, 6, 450]
])

# Extracting the price column (index 2)
prices = sales_data[:, 2]

# Calculating average price
average_price = np.mean(prices)

print("Average Price of Products Sold:", average_price)
