#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash

#importing files that I created. 
from database import * 
from users import *

#Setting up Flask
app = Flask(__name__)

#This route takes the user to the home page
@app.route('/', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        #Recieving the information from the user.
        username = request.form['username']
        password = request.form['password']
        #creating the db connection object
        db = Connection()
        #Checking to see if the user is in the database.
        flag, not_found, password_no_match = db.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('home'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            if not_found:
                flash('Username not found, maybe sign up!')
            elif password_no_match:
                flash('Password does not match! Maybe sign up!')
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

#This route will take the user to the home page 
@app.route('/home')
def home():
    see_nav_footer = True
    return render_template('home.html', see_nav_footer = see_nav_footer)

#This route will take the user to the create table page 
@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    see_nav_footer = True
    if request.method == 'POST':
        #Receiving all of the data from the user. 
        table_name = request.form['table_name']
        value1 = request.form['mytext[]']
        data_type_1 = request.form.get('data_type')
        value2 = request.form.get('mytext2')
        data_type_2 = request.form.get('data_type_2')
        value3 = request.form.get('mytext3')
        data_type_3 = request.form.get('data_type_3')
        value4 = request.form.get('mytext4')
        data_type_4 = request.form.get('data_type_4')
        value5 = request.form.get('mytext5')
        data_type_5 = request.form.get('data_type_5')
        value6 = request.form.get('mytext6')
        data_type_6 = request.form.get('data_type_6')
    return render_template('create_table.html', see_nav_footer = see_nav_footer)

#This route will sign out the user 
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    #Redirect to Landing page
    return redirect(url_for('landing'))

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)