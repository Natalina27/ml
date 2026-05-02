# Coding Exercise 4: Dataset Splitting and Feature Scaling

In this exercise, you will split the Iris dataset into training and test sets, then apply feature scaling.

## Task

1. Import the required libraries: `pandas`, `train_test_split`, and `StandardScaler`.
2. Load the Iris dataset using `pd.read_csv`. The dataset file is named `iris.csv`.
3. Use `train_test_split` to split the dataset into an 80-20 training-test set.
4. Apply `random_state=42` in `train_test_split` for reproducible results.
5. Print `X_train`, `X_test`, `y_train`, and `y_test` to understand the dataset split.
6. Use `StandardScaler` to apply feature scaling on the training and test sets.
7. Print the scaled training and test sets to verify feature scaling.

## Dataset

Place `iris.csv` in this folder before running the solution.

## Run

From this folder:

```bash
python3 solution.py
```
