#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import xlrd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pickle

# Read the divorce dataset downloaded from http://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set
df = pd.read_csv("divorce.csv", sep=";", engine='python')
print(df)

# The values have various ranges. Normalizing Dataset so that the values are distributed between 0 to 1.
X = df.values[:,0:54]
Y = df.values[:,54]
standard_deviation = np.std(X,axis = 0)
mean = np.mean(X,axis = 0)
X = X-mean/standard_deviation
standard_deviation.shape

# Split the Divirce dataset Into Training And Testing Datasets to help determine the accuracy of the model later.
# X values are the attribute values (answers to the 54 questions)
# Y values are the divorce outcome (Yes/No or 1/0) provided in the 55th column in the Divorce dataset
# training values are the training dataset values
# testing values are for testing datasets values
#
# X_training - Attribute values in the training dataset
# Y_training - Divorce outcomes for the training dataset
# X_testing - Attribute values in the testing dataset
# Y_testing - Divorce outcomes for the testing dataset

from sklearn.model_selection import train_test_split
X_training, X_testing, y_training, y_testing = train_test_split( X, Y, test_size=0.25, random_state=42)

# Logistic Regression Algorithm
from sklearn.linear_model import LogisticRegression
lg = LogisticRegression(random_state=0,solver = "liblinear")
# Create Model
lg.fit(X_training,y_training)
# Predict outcome using the Attribute values from the testing dataset
y_predict = lg.predict(X_testing)
# Compute Accuracy of the model
print("Accuracy = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

print (y_testing)

print (y_predict)

# Write this model to a file to be used during production inferencing
training_model_file = 'divorce_prediction_model-Logistic_Regression_Algo.model'
pickle.dump(lg, open(training_model_file, 'wb'))
print("Wrote divorce prediction model to file", training_model_file)
