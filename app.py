#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/')
def landing():
    return render_template('index.html')

#This route takes the user to the sign up page 
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  if request.method == 'POST':
        #Pulling data from the form on the signup page
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        password2 = request.form['password2']
  return render_template('signup.html')

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)