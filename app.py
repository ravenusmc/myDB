#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/')
def landing():
    return render_template('index.html')

#This route takes the user to the sign up page 
@app.route('/signup')
def signup():
    return render_template('signup.html')

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)