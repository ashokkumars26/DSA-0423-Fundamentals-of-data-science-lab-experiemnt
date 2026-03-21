import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Dataset
data = {
    'Weight': [150,170,120,160,180,110],
    'Color': ['Red','Orange','Yellow','Red','Orange','Yellow'],
    'Texture': ['Smooth','Rough','Smooth','Smooth','Rough','Smooth'],
    'Type': ['Apple','Orange','Banana','Apple','Orange','Banana']
}

df = pd.DataFrame(data)

# Encoding categorical features
le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

df['Color'] = le_color.fit_transform(df['Color'])
df['Texture'] = le_texture.fit_transform(df['Texture'])
df['Type'] = le_type.fit_transform(df['Type'])

# Features and target
X = df[['Weight','Color','Texture']]
y = df['Type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# kNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Accuracy
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# New fruit data (example)
# Example: Weight=140, Color=Yellow, Texture=Smooth
new_data = pd.DataFrame({
    'Weight': [140],
    'Color': le_color.transform(['Yellow']),
    'Texture': le_texture.transform(['Smooth'])
})

# Prediction
prediction = model.predict(new_data)

# Decode result
predicted_fruit = le_type.inverse_transform(prediction)

print("Predicted Fruit Type:", predicted_fruit[0])
