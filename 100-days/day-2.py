# -*-coding:utf-8-*-
# Edited by bighead 19-2-8

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

########## Data preprocessing
dataset = pd.read_csv("Data/studentscores.csv").values
X = dataset[:, :1]
Y = dataset[:, 1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=233)
##########END

########## Fit the simple linear regression model to the training set
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
##########END

########## Predicting the result
Y_pred = regressor.predict(X_test)
##########END

########## Plot the result
# ##### Train
# plt.scatter(X_train, Y_train, color='red')
# plt.plot(X_train, regressor.predict(X_train), color='blue')
# plt.show()
# #####END

# ##### Test
# plt.scatter(X_test, Y_test, color='red')
# plt.plot(X_test, regressor.predict(X_test), color='blue')
# plt.show()
# #####END

##### all data
plt.scatter(X, Y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.show()
#####END

##########END
