import pandas as pd

# Raw survey data (with errors - dirty data)
data = {
    "Student_ID": range(1, 11),
    "Choice": ["Veggie Wrap", "Chicken Burger", "veggie wrap",
               "Chiken Burger", "Pasta Salad", "Veggie wrap",
               "Chicken burger", "Pasta salad", "Veggie Wrap",
               "Chicken Burger"]
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# -------------------------------
# DATA CLEANING
# -------------------------------

# Convert to lowercase for consistency
df["Choice"] = df["Choice"].str.lower()

# Fix spelling mistakes
df["Choice"] = df["Choice"].replace({
    "chiken burger": "chicken burger"
})

# Standardize format (title case)
df["Choice"] = df["Choice"].str.title()

print("\nCleaned Data:\n")
print(df)

# -------------------------------
# ANALYSIS
# -------------------------------

# Count preferences
counts = df["Choice"].value_counts()

print("\nFood Preference Count:\n")
print(counts)
