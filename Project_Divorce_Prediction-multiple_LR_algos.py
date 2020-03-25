#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import xlrd
import pickle

# Read the divorce dataset downloaded from
# http://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set
df = pd.read_csv("divorce_data/divorce.csv")
df

# The values have various ranges. Normalizing Dataset so that the values
# are distributed between 0 to 1.
X = df.values[:,0:54]
Y = df.values[:,54]
standard_deviation = np.std(X,axis = 0)
mean = np.mean(X,axis = 0)
X = X-mean/standard_deviation
standard_deviation.shape

# Split the Divirce dataset Into Training And Testing Datasets to help
# determine the accuracy of the model later.
#
# X values are the attribute values (answers to the 54 questions)
# Y values are the divorce outcome (Yes/No or 1/0) provided in the
#   Class (55th) column in the Divorce dataset
# training values are the training dataset values
# testing values are for testing datasets values
#
# X_training - Attribute values in the training dataset
# y_training - Divorce outcomes for the training dataset
# X_testing - Attribute values in the testing dataset
# y_testing - Divorce outcomes for the testing dataset

from sklearn.model_selection import train_test_split
X_training, X_testing, y_training, y_testing = train_test_split( X, Y, test_size=0.25, random_state=42)

# Logistic Regression Algorithm
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection

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

# Naive Bayes Algorithm: Using the training and testing datasets, find
# the accuracy of the algorithm
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_training, y_training)
y_predict = nb.predict(X_testing)
print("Model Accuracy = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

print(y_predict)

# K-Nearest Neighbors (KNN) Algorithm: Using the training and testing
# datasets, rind the accuracy of the algorithm
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 15)
knn.fit(X_training, y_training)
y_predict = knn.predict(X_testing)
print("Accuracy (K-Nearest Neighbors (KKN) Algorithm) = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

# Decision Tree Algorithm: Using the training and testing datasets,
# rind the accuracy of the algorithm
from sklearn.tree import DecisionTreeClassifier
decisiontree = DecisionTreeClassifier(max_depth = 10, random_state = 101, max_features = None, min_samples_leaf = 15)
decisiontree.fit(X_training,y_training)
y_predict = decisiontree.predict(X_testing)
print("Accuracy (Decision Tree Algorithm) = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

# Random Forest Algorithm: Using the training and testing datasets,
# rind the accuracy of the algorithm
from sklearn.ensemble import RandomForestClassifier
randomforest = RandomForestClassifier(n_estimators = 70, oob_score = True, n_jobs = -1, random_state = 101, max_features = None, min_samples_leaf = 30)
randomforest.fit(X_training, y_training)
y_predict = randomforest.predict(X_testing)
print("Accuracy (Rabdom Forest Classifier Algorithm) = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

# Support Vector Machine (SVM) Algorithm: Using the training and
# testing datasets, rind the accuracy of the algorithm
from sklearn.svm import SVC
svm = SVC(kernel = "linear", C = 0.025, random_state = 101)
svm.fit(X_training,y_training)
y_predict = svm.predict(X_testing)
print("Accuracy (Support Vector Machine (SVM) Algorithm) = ",((np.sum(y_predict==y_testing)/y_testing.shape[0])*100),"%",sep="")

# Neural Networks Algorithm: Using the training and testing datasets,
# rind the accuracy of the algorithm
from keras.models import Sequential
from keras.layers import Dense
neuralnet = Sequential()
neuralnet.add(Dense(128, activation = "relu", input_dim=X_training.shape[1]))
neuralnet.add(Dense(64, activation = "relu"))
neuralnet.add(Dense(32, activation = "relu"))
neuralnet.add(Dense(1, activation = "sigmoid"))
neuralnet.summary()
neuralnet.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ["accuracy"])
neuralnet.fit(X_training, y_training, epochs=10, batch_size=2000)
accuracy = neuralnet.evaluate(X_testing, y_testing)[1]
print('Accuracy (Neural Network Algorithm): %.2f' % (accuracy*100))

# Further enhancement: Rank the algorithms according to their accuracy metrics.
#
# Compute the Confusion Matrix based on the actual and predicted divorce outcomes
# Find the accuracy score taking the actual and predicted values
# Generate a Classification report
#
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
actual = y_testing
predicted = y_predict 
results = confusion_matrix(actual, predicted) 
print('Confusion Matrix :')
print(results) 
print('Accuracy Score :',accuracy_score(actual, predicted)) 
print('Report : ')
print(classification_report(actual, predicted)) 

# PRODUCTION Divorce Prediction
#
# Predict Divorce outcome for one subject based on the production values
# entered on the website.
#
# A new user goes to the Divorce Prediction webpage and answers the
# questionaire of 54 questions.
# The HTML5 code of the webpage writes the values into a CSV file.
# This CSV file read here and the Divorce outcome is predicted based
# on the production values provided.

# Read Production Data of one subject
pdf = pd.read_csv("divorce_data/production.csv")
pdf

# Normalizing Production Data and splitting it into Attributes and Outcome
Xp = pdf.values[:,0:54]
Yp = pdf.values[:,54]

# Since Logistic Regression Algorithm provided the highest accuracy (100%),
# we will use it to predict production data
from sklearn.linear_model import LogisticRegression

# Read the Machine Learning model from a file use for production inferencing
prod_model_file = 'divorce_prediction_model-Logistic_Regression_Algo.model'
print("Trying to read divorce prediction model from file", prod_model_file) 
prod_model = pickle.load(open(prod_model_file, 'rb'))
print("Successfully read divorce prediction model from file:", prod_model_file) 
prod_model_score_verify = prod_model.score(X_testing, y_testing)
print("Verifying production model score")
print(prod_model_score_verify)

#klg = LogisticRegression(random_state=0,solver = "liblinear")
#klg.fit(X_training,y_training)
y_predict = prod_model.predict(Xp)
print("Prediction (0 - not divorced, 1 - divorced) = ", y_predict)
print("Actual Divorced or not (0 - not divorced, 1 - divorced) = ", Yp)
print("Accuracy (Logistic Regression Algorithm) = ",((np.sum(y_predict==Yp)/y_testing.shape[0])*100),"%",sep="")
