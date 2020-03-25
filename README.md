### Final Project
# Divorce Prediction

## These files address the following workflow

### Learning Stage:-
Get Dataset ==> Apply ML and create Model ==> Test Model ==> Compute Accuracy ==> Save Model

### Inference/Prediction Stage:-
Get inference data ==> Read Model ==> Predict outcome based on inference data ==> Display outcome to user

### Contents of the files:-
* divorce.csv - Divorce training/test dataset downloaded from http://archive.ics.uci.edu/ml/datasets/Divorce+Predictors+data+set

* mord_ml.py - ML logic program file to read divorce.csv dataset, split dataset to train and test, apply Logistic Regression to the training dataset and create model, use model to predict test dataset, compute accuracy of model, save model to a file. This stage is used by data scientists to create and tune models.

* divorce_prediction_model-Logistic_Regression_Algo.model - File where the Logistic Regression model is saved.

* production.csv - The response of a single user who wants to predict getting divorced or staying married.

*mord_in.py - The inferencing/prediction program to read the logistic regression model file, read the production.csv file and predict divorce (=1) or stay together (=0).
