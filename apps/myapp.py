from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from ml import forecast

app = Flask(__name__)
# Set up connection
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

with open('indicators.txt', 'r') as file:
    questions = file.read().splitlines()
indexes = [f'attr{i}' for i in range(1,len(questions)+1)]
zip_list = zip(indexes, questions)

@app.route('/')
def index():
    return render_template('index1.html', zip_list=zip_list)

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
            return render_template('submit.html', result=result)
        except:
            return "Error: Please answer all questions"
    else:
        return "Error"


if __name__ == "__main__":
    app.run(debug=True)