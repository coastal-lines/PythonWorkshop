#iris

import sklearn
import pandas as pd
import numpy as np
import mglearn
from pandas.plotting import scatter_matrix
import tkinter

#load data
from sklearn.datasets import load_iris
iris_dataset = load_iris()
#print("Keys for iris_dataset: \n{}".format(iris_dataset.keys()))
#print("Features names: \n{}".format(iris_dataset['feature_names']))
#print(iris_dataset['data'])

#split training and test data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                           marker='o', hist_kwds={'bins': 20}, s=60,
                           alpha=.8, cmap=mglearn.cm3)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
print(f"Predict is {iris_dataset['target_names'][prediction]}")

y_pred = knn.predict(X_test)
print(f"Occurancy is: {knn.score(X_test, y_test)}")

top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()