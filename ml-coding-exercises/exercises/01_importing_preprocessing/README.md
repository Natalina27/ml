# Exercise 1: Importing and Preprocessing a Dataset

In this exercise, you will explore data preprocessing with Python.

## Task

1. Import the required libraries:
   - `pandas`
   - `numpy`
   - `train_test_split` from `sklearn.model_selection`
2. Load the Iris dataset from `iris.csv` into a DataFrame named `dataset`.
3. Split the dataset into:
   - `X`: matrix of features, all columns except the last one.
   - `y`: dependent variable vector, the last column.
4. Use `.values` to convert pandas objects into NumPy arrays.
5. Print `X` and `y`.

## Run

From this folder:

```bash
python solution.py
```
