import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the data
file_path = Path('divorce.csv')
divorce_df = pd.read_csv(file_path, sep=';')

# Drop the null rows
divorce_df = divorce_df.dropna()

# Create our features
X = divorce_df.drop(columns='Class')

# Create our target
y = divorce_df['Class'].copy()

# Create X_train, X_test, y_train, y_test
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# Logistic Regression
classifier = LogisticRegression(solver='lbfgs', random_state=1, max_iter=200)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)

def forecast(answers):
    prediction = classifier.predict(answers)
    if prediction ==1:
        result = 'divorced'
    else:
        result ='still married'
    return (result)


