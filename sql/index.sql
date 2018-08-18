--This file contains the code that will be used to set up MySQL

--Creating the database
-- CREATE DATABASE myDB;

--See the table 
DESCRIBE USERS;

--Creating the users table
CREATE TABLE users (
    user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(255) NOT NULL
);

--This table will hold all of the data for the users. 
CREATE TABLE user_tables (
  table_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  tableName VARCHAR(30) NOT NULL,
  CONSTRAINT user_tablesFKusers
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE students (
            item_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            firstname varchar(30) NOT NULL,
            lastname varchar(30) NOT NULL,
  ) 


drop table users;