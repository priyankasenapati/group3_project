#!/usr/bin/env python
# coding: utf-8
    
import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

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
# Divorce outcome is predicted based on the production values provided.
#

# Read the Machine Learning model from a file use for production inferencing
file = 'divorce_prediction_model-Logistic_Regression_Algo.model'
print("Loading ML model from file: ", file)
lg = pickle.load(open(file, 'rb'))

def forecast(answers):
    print("Predicting Stay Married or Will be Divorced")
    prediction = lg.predict(answers)
    if prediction ==1:
        result = 'divorced'
    else:
        result ='still married'
    return (result)
