#This file will set up the users class which will allow the user to sign in. 

class Users():

    def __init__(self, firstname, lastname, email, username, hashed):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password_hashed = hashed