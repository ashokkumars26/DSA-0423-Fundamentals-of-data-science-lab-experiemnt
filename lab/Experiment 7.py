import numpy as np

# Creating NumPy array
house_data = np.array([
    [3, 1500, 300000],
    [5, 2500, 550000],
    [4, 1800, 400000],
    [6, 3200, 750000],
    [2, 1200, 200000],
    [5, 2700, 600000]
])

# Filtering houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Extracting sale prices
sale_prices = filtered_houses[:, 2]

# Calculating average sale price
average_price = np.mean(sale_prices)

print("Average Sale Price of Houses with More Than 4 Bedrooms:", average_price)
