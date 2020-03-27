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

### I have also added Divorce Prediction Sample Images
### I have added Divorce prediction multiple LR models applied to divorce.csv dataset.


-------------------------------------------------------------------------------------------------------------------------

### Talking Points For My  Slides I Had Created For Final Presenation To The Class:
* First Slide :-
<img width="703" alt="Screen Shot 2020-03-27 at 12 22 56 PM" src="https://user-images.githubusercontent.com/55486501/77729982-e79abc80-7025-11ea-813a-899f171546bf.png">

1-So as you can see the input to the model training evaluation analysis workflow is cleaned and prep data 

 2- This data is now split in to training and testing data .
The learning  engine first takes the training data and creates the ML model  using the ML algorithm.

3-Then it takes the testing data to evaluate the accuracy of a model. These two step of learning and testing is repeated using additional dataset to tune the model to increase its accuracy.

4-Once the model has reached the expected accuracy level , the model is exported out 
so that it can be used by other applications .

* Second Slide :-
<img width="673" alt="Screen Shot 2020-03-27 at 12 23 10 PM" src="https://user-images.githubusercontent.com/55486501/77730069-0e58f300-7026-11ea-91e9-98d619c69c8d.png">

Workflow
I wanted to go lil bit deeper in  to the data workflow…

First  the data is normalized between 0 and 1 

(Normalization: THERE MIGHT BE DIFFERENT VALUE RANGES FOR DIFFERENT SECTIONS OF THE DATA. ONE RANGE CAN BE BETWEEN 0 TO 5 WHILE ANOTHER CAN BE BETWEEN 0 TO 10. SO THE ABSOLUTE VALUES CAN’T BE COMPARED)

2- The data is split 75 % and 25 % in to training and testing data respectively. The more the data size the better it is for training.

3-The specific algorithm is selected to fit the training data. And create a model.

4-Now this model is applied on the testing data to predict  the outcome.

5-Using the  existing outcome from the training  data set and the predicted outcome from the testing data set, accuracy of the model is computed.

6-We all generate confusion matrix to analyze false positives and  false negatives.

7-We do the above step repeatedly using different data set until we achieve the desire accuracy of the model.

After getting the maximum accuracy from all the models. We choose the best model to be used for production.

* 3rd Slide:

<img width="705" alt="Screen Shot 2020-03-27 at 12 23 21 PM" src="https://user-images.githubusercontent.com/55486501/77730105-23358680-7026-11ea-8254-9ec0d920490c.png">


After comparing the accuracy for all the models we found that the logistic regression model  and the neural network model gave 100 % accuracy score. WE choose the logistic regression model for production and exported the model into a file.

* 4th Slide:

<img width="674" alt="Screen Shot 2020-03-27 at 12 23 34 PM" src="https://user-images.githubusercontent.com/55486501/77730146-36e0ed00-7026-11ea-995a-8f1f46388e96.png">
These are other machine learning algorithms we tested with …..

* 5th Slide:

<img width="686" alt="Screen Shot 2020-03-27 at 12 23 45 PM" src="https://user-images.githubusercontent.com/55486501/77730182-4bbd8080-7026-11ea-8adc-2fb659019d14.png">

This slide shows how application use the model for inferencing  real world data(answers obtained  for the questions asked to  the user).

The applications can be drones ,self driving cars , cell phones and others  .




