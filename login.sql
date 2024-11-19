CREATE DATABASE login_db; 

USE login_db ;

CREATE TABLE masuk  (
    username VARCHAR(15) NOT NULL,
    npm VARCHAR(10) NOT NULL,
    password VARCHAR(25) NOT NULL
    
);
INSERT INTO users (username, npm, password ) VALUES ('yahya', '25', "$2b$12$12345Hash");


