import pandas as pd

# Creating dataset
data = {
    'City': ['Chennai', 'Chennai', 'Chennai',
             'Delhi', 'Delhi', 'Delhi',
             'Mumbai', 'Mumbai', 'Mumbai'],
    'Temperature': [30, 32, 31, 20, 25, 22, 28, 29, 30]
}

df = pd.DataFrame(data)

# Mean temperature for each city
mean_temp = df.groupby('City')['Temperature'].mean()

# Standard deviation for each city
std_temp = df.groupby('City')['Temperature'].std()

# Temperature range (max - min)
temp_range = df.groupby('City')['Temperature'].max() - df.groupby('City')['Temperature'].min()

# City with highest temperature range
highest_range_city = temp_range.idxmax()

# City with lowest standard deviation
most_consistent_city = std_temp.idxmin()

# Display results
print("Mean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print("\nTemperature Range:\n", temp_range)
print("\nCity with Highest Temperature Range:", highest_range_city)
print("City with Most Consistent Temperature:", most_consistent_city)
