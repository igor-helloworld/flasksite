#IMPORTS
from flask import Flask, render_template,request, redirect
import flask

app = Flask(__name__)
#APP ROUTES

@app.route('/')
def main_page():
    return render_template('index.html')

@app.route('/bins')
def bins_page():
    return render_template('bins.html')

@app.route('/protecttheenvironment')
def protect():
    return render_template('protect.html')
    

if __name__ == 'main':
    app.run(debug=True)
