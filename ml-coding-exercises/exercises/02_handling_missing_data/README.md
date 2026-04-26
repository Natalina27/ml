# Exercise 2: Handling Missing Data in a Dataset

In this exercise, you will handle missing data in the Pima Indians Diabetes dataset.

## Task

1. Import the required preprocessing libraries, including `SimpleImputer`.
2. Load `pima-indians-diabetes.csv` into a pandas DataFrame.
3. Identify missing data and print the number of missing entries in each column.
4. Replace missing values with the mean value of each numerical column.
5. Apply `fit` and `transform` from `SimpleImputer`.
6. Update the matrix of features.
7. Print the updated matrix of features.

## Dataset

Place `pima-indians-diabetes.csv` in this folder before running the solution.

In this dataset, some medical measurements use `0` to represent missing values. The solution treats zeros as missing values for feature columns except the first feature and the target column.

## Run

From this folder:

```bash
python solution.py
```
