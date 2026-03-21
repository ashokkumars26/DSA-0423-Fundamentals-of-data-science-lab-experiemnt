import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Creating dataset
data = {
    'Customer_ID': [101,102,103,104,105,106],
    'Total_Spent': [500,1500,300,2000,800,1200],
    'Visit_Frequency': [5,12,3,15,7,10]
}

df = pd.DataFrame(data)

# Selecting features
X = df[['Total_Spent','Visit_Frequency']]

# Applying K-Means
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(X)

print(df)

# Visualizing clusters
plt.scatter(df['Total_Spent'], df['Visit_Frequency'], c=df['Cluster'])
plt.xlabel("Total Spent")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation using K-Means")
plt.show()
