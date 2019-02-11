# -*-coding:utf-8-*-
# Edited by bighead 19-2-9

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

########## Load the data
dataset = pd.read_csv("Data/50_Startups.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values
# print("X: \n{}".format(X))
# print("Y: \n{}".format(Y))
##########END

########## Encoding the categorical data
labelEncoder = LabelEncoder()
X[:, -1] = labelEncoder.fit_transform(X[:, 3])
oneHotEncoder = OneHotEncoder(categorical_features = [3])
X = oneHotEncoder.fit_transform(X).toarray()
X = X[:, 1:]
##########END

########## Train Test Split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=233)
#########END

########## fitting model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
##########END

########## Predict
y_pred = regressor.predict(X_test)
print("label: {}".format(Y_test))
print("predict: {}".format(y_pred))
##########END

########## PLOT
## do not know how to plot more dimension data
##########END
