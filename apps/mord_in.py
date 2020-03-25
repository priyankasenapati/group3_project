#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import xlrd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets
import pickle

# PRODUCTION Divorce Prediction
#
# Predict Divorce outcome for one subject based on the production values entered on the website.
#
# A new user goes to the Divorce Prediction webpage and answers the questionaire of 54 questions.
# The HTML5 code of the webpage writes the values into a CSV file. This CSV file read here and the
# Divorce outcome is predicted based on the production values provided.
#

# Read Production Data of one subject
pdf = pd.read_csv("production.csv", sep=",", engine='python')
pdf

# Normalizing Production Data and splitting it into Attributes and Outcome
Xp = pdf.values[:,0:54]


# Read the Machine Learning model from a file use for production inferencing
file = 'divorce_prediction_model-Logistic_Regression_Algo.model'
print("Loading ML model from file: ", file)
lg = pickle.load(open(file, 'rb'))

print("Predicting Stay Married or Will be Divorced")
y_predict = lg.predict(Xp)
print("Prediction (0 - not divorced, 1 - divorced) = ", y_predict)
