from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from ml import forecast

# Add SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from config import db_password

app = Flask(__name__)
# Set up database
#-----------------------------
ENV = 'PythonData'

if ENV == 'PythonData':
    app.debug = True
    db_string = f'postgres://postgres:{db_password}@127.0.0.1:5432/divorce_prediction'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_string
    print("success")
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    print("error")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Ques(db.Model):
    __tablename__ = 'ques'
    id = db.Column(db.String, primary_key=True)
    question = db.Column(db.String, nullable=False)
    answer = db.Column(db.Integer, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        

#--------------------------------

# Create question dataframe and save to questions_table table
with open('indicators.txt', 'r') as file:
    questions = file.read().splitlines()
indexes = [f'attr{i}' for i in range(1,len(questions)+1)]
zip_list = zip(indexes, questions)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/survey')
def survey():
    # zip indexes and questions and pass to html 
    zip_list = zip(indexes, questions)
    return render_template('survey.html', zip_list=zip_list)

@app.route('/submit', methods=['GET','POST'])
def submit():
    attributes = []
    if request.method == 'POST':  
        try:
            for index in indexes:
                value = request.form[index]
                attributes.append(value)
            attributes = pd.DataFrame([attributes], columns=indexes)
            # Run machine learning model
            result = forecast(attributes)
            if(result == "divorced"):
                return render_template('submit_divorce.html', result = result)
            else :
                return render_template('submit_success.html', result = result)
        except:
            return "Error: Please answer all questions"
    else:
        return "Error"



if __name__ == "__main__":
     app.run(debug=True)
