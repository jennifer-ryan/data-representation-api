/* Creating database and tables*/

CREATE DATABASE plantdb;

CREATE TABLE plantprices (
    -> type varchar(250) PRIMARY KEY NOT NULL,
    -> price decimal(6,2) NOT NULL
    -> );

CREATE TABLE plantinfo (
    -> id int AUTO_INCREMENT NOT NULL,
    -> name varchar(250) NOT NULL,
    -> scientific_name varchar(250),
    -> light_needs varchar(250),
    -> water_needs varchar(250),
    -> type varchar(250) NOT NULL,
    -> stock int,
    -> PRIMARY KEY (id),
    -> FOREIGN KEY (type) REFERENCES plantprices(type)
    -> );