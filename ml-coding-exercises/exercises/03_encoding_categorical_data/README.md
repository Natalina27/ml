# Coding Exercise 3: Encoding Categorical Data for Machine Learning

In this exercise, you will encode categorical data in the Titanic dataset before using it in a machine learning model.

## Task

1. Import the required libraries: `pandas`, `numpy`, `ColumnTransformer`, `OneHotEncoder`, and `LabelEncoder`.
2. Load the Titanic dataset into a pandas DataFrame using `pd.read_csv`. The dataset file is named `titanic.csv`.
3. Identify the categorical features in the dataset that need to be encoded. Store these feature names in a list for easy access later.
4. Create an instance of the `ColumnTransformer` class to apply `OneHotEncoder` to the categorical features.
5. Use the `fit_transform` method on the `ColumnTransformer` instance to apply one-hot encoding.
6. Convert the output of `fit_transform` into a NumPy array for further use.
7. Encode the `Survived` column, which is the dependent binary categorical variable, using `LabelEncoder`.
8. Print the updated matrix of features and the dependent variable vector.

## Dataset

Place `titanic.csv` in this folder before running the solution.

## Run

From this folder:

```bash
python solution.py
```
