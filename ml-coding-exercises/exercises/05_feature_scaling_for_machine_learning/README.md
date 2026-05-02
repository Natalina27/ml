# Coding Exercise 5: Feature Scaling for Machine Learning

In this exercise, you will load the Wine Quality Red dataset, split it into training and test sets, and apply feature scaling.

## Task

1. Import the required libraries: `pandas`, `train_test_split`, and `StandardScaler`.
2. Load the Wine Quality Red dataset using `pd.read_csv` with the correct delimiter (`;`).
3. Separate the dataset into features (`X`) and target (`y`), where the target is `Quality`.
4. Split the dataset into an 80-20 training-test set using `random_state=42`.
5. Create an instance of `StandardScaler`.
6. Fit the scaler on the training features and transform the training set using `fit_transform`.
7. Transform the test set using `transform`.
8. Print the scaled training and test datasets.

## Dataset

Place `winequality-red.csv` in this folder before running the solution.

## Run

From this folder:

```bash
python3 solution.py
```
