/* Creating database and tables*/

CREATE DATABASE plantdb;

CREATE TABLE plantprices (
    -> type varchar(250) PRIMARY KEY,
    -> price int
    -> );

CREATE TABLE plantinfo (
    -> id int AUTO_INCREMENT,
    -> name varchar(250),
    -> scientific_name varchar(250),
    -> light_needs varchar(250),
    -> water_needs varchar(250),
    -> type varchar(250),
    -> stock int,
    -> PRIMARY KEY (id),
    -> FOREIGN KEY (type) REFERENCES plantprices(type)
    -> );