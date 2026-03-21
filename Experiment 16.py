import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Creating dataset
data = {
    'Age': [45, 50, 39, 60, 42],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Blood_Pressure': [130, 150, 120, 160, 135],
    'Cholesterol': [200, 240, 180, 260, 210],
    'Outcome': ['Good', 'Bad', 'Good', 'Bad', 'Good']
}

df = pd.DataFrame(data)

# Encoding categorical values
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Outcome'] = le.fit_transform(df['Outcome'])

# Features and target
X = df[['Age', 'Gender', 'Blood_Pressure', 'Cholesterol']]
y = df['Outcome']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Predicted Outcome:", predictions)
print("Model Accuracy:", accuracy)
