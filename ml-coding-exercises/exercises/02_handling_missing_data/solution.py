# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
dataset = pd.read_csv("pima-indians-diabetes.csv")
X_before = dataset.iloc[:, :-1].values
print(X_before[:5])
print('--------------------------------')
print('--------------------------------')
# Identify missing data (assumes that missing data is represented as NaN)
# Replace 0 with NaN in the columns with missing data
columns_with_zero_as_missing = dataset.columns[1:-1]
dataset[columns_with_zero_as_missing] = dataset[columns_with_zero_as_missing].replace(
    0,
    np.nan,
)

# Print the number of missing values in each column
print(dataset.isnull().sum())
print('--------------------------------')
# Creating the matrix of features (X) and the dependent variable vector (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X[:5])
print('--------------------------------')

# Configure an instance of the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# Fit the imputer on the features and transform the features
X[:, 1:-1] = imputer.fit_transform(X[:, 1:-1])


# Print the updated matrix of features
# print(np.isnan(X).sum(axis=0))
# print(X)
# print(y)
print('--------------------------------')
print(X[:5])
print('--------------------------------')

# print(X.shape)

