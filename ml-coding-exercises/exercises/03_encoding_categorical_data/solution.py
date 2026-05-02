# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
dataset=pd.read_csv('titanic.csv')

# Identify the categorical data
# categorical_features = [
#     column
#     for column in dataset.select_dtypes(include=["object"]).columns
#     if dataset[column].nunique() < 20
# ]
categorical_features = ["Sex", "Embarked", "Pclass"]

# print(categorical_features)

# Implement an instance of the ColumnTransformer class
ct = ColumnTransformer(
    transformers=[
        ("encoder", OneHotEncoder(), categorical_features)
    ],
    remainder="passthrough"
)

# Apply the fit_transform method on the instance of ColumnTransformer
X = dataset.drop("Survived", axis=1)
y = dataset["Survived"]

X = ct.fit_transform(dataset)

# Convert the output into a NumPy array
X = np.array(X)


# Use LabelEncoder to encode binary categorical data
le = LabelEncoder()
y = le.fit_transform(y)

# Print the updated matrix of features and the dependent variable vector
print(X)
print(y)