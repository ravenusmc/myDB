#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#importing files that I created. 
from database import * 
from users import *

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
      password = request.form['password1']
      password2 = request.form['password2']
      if password != password2:
            flash('Passwords Do Not Match!') 
      else:
            #creating the db object to interact with the db.  
            db = Connection()
            #Encrypting the password
            password, hashed = db.encrypt_pass(password)
            #creating user object
            user = Users(firstname, lastname, email, username, hashed)
            #Adding the user to the database
            db.insert_user(user)
            print('User Inserted')

  return render_template('signup.html')

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)