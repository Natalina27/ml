import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


dataset = pd.read_csv("iris.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(X)
print(y)
