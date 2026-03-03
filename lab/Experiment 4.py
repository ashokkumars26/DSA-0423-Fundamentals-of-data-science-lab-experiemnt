import pandas as pd

# Creating dataset
data = {
    'Property_ID': [1, 2, 3, 4, 5],
    'Location': ['Mumbai', 'Delhi', 'Mumbai', 'Chennai', 'Delhi'],
    'Bedrooms': [3, 5, 4, 2, 6],
    'Area_sqft': [1200, 2500, 1800, 900, 3200],
    'Listing_Price': [15000000, 30000000, 22000000, 10000000, 45000000]
}

property_data = pd.DataFrame(data)

avg_price_location = property_data.groupby('Location')['Listing_Price'].mean()

properties_more_than_4 = property_data[property_data['Bedrooms'] > 4].shape[0]

largest_property = property_data.loc[property_data['Area_sqft'].idxmax()]

print("Average Listing Price by Location:\n", avg_price_location)
print("\nNumber of Properties with more than 4 Bedrooms:", properties_more_than_4)
print("\nProperty with the Largest Area:\n", largest_property)
