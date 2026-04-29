# Importing the necessary libraries
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

# Load the dataset
dataset = pd.read_csv("pima-indians-diabetes.csv")

# Identify missing data
print(dataset.isnull().sum())

# Creating the matrix of features (X) and the dependent variable vector (y)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Configure an instance of the SimpleImputer class
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")

# Fit the imputer on the features and transform the features
X = imputer.fit_transform(X)

# Print the updated matrix of features
print(X)
