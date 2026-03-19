import pandas as pd
import numpy as np

# -----------------------------
# Step 1: Load Dataset
# -----------------------------
# Replace 'sales_data.csv' with your file path
df = pd.read_csv('sales_data.csv')

print("Initial Data:")
print(df.head())

# -----------------------------
# Step 2: Handle Missing Data
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values with mean
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Quantity'] = df['Quantity'].fillna(df['Quantity'].median())

# Fill categorical missing values with mode
df['Region'] = df['Region'].fillna(df['Region'].mode()[0])
df['Product'] = df['Product'].fillna(df['Product'].mode()[0])

# -----------------------------
# Step 3: Feature Engineering
# -----------------------------
# Convert Order Date to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create new columns
df['Month'] = df['Order Date'].dt.month
df['Year'] = df['Order Date'].dt.year

# Revenue per unit
df['Revenue_per_Unit'] = df['Sales'] / df['Quantity']

# -----------------------------
# Step 4: Basic Analysis
# -----------------------------
# Total Sales
total_sales = df['Sales'].sum()
print("\nTotal Sales:", total_sales)

# Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()
print("\nSales by Region:")
print(sales_by_region)

# Top 5 Products
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 Products:")
print(top_products)

# -----------------------------
# Step 5: Filtering
# -----------------------------
# High-value transactions (> 1000)
high_sales = df[df['Sales'] > 1000]
print("\nHigh Value Transactions:")
print(high_sales.head())

# -----------------------------
# Step 6: Pivot Table Analysis
# -----------------------------
pivot_table = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    columns='Month',
    aggfunc='sum'
)

print("\nPivot Table (Sales by Region & Month):")
print(pivot_table)

# -----------------------------
# Step 7: Insights
# -----------------------------
print("\n--- Business Insights ---")
print("1. Best performing region:", sales_by_region.idxmax())
print("2. Best selling product:", top_products.idxmax())
print("3. Average revenue per unit:", df['Revenue_per_Unit'].mean())

# -----------------------------
# Step 8: Save Processed Data
# -----------------------------
df.to_csv('processed_sales_data.csv', index=False)
print("\nProcessed data saved successfully!")
