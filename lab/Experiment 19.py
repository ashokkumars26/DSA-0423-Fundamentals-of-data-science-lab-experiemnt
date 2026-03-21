import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Creating dataset
data = {
    'Customer_ID': [1,2,3,4,5,6,7,8],
    'Total_Spent': [200, 1500, 300, 2500, 800, 1200, 400, 2200],
    'Items_Purchased': [2, 10, 3, 15, 6, 9, 4, 13]
}

df = pd.DataFrame(data)

# Selecting features
X = df[['Total_Spent', 'Items_Purchased']]

# Applying K-Means
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(X)

# Display clustered data
print(df)

# Plotting clusters
plt.scatter(df['Total_Spent'], df['Items_Purchased'], c=df['Cluster'])
plt.xlabel("Total Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means")
plt.show()
    
