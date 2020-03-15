from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# Set up connection
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sumbit')
def submit():
    return "Successful"


if __name__ == "__main__":
    app.run(debug=True)