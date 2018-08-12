#This file will set up the users class 

class User():

    def __init__(self, firstname, lastname, email, username, password, hashed):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password
        self.password_hashed = hashed