/* Creating database and tables*/

CREATE DATABASE plantdb;

CREATE TABLE plantprices (
    -> plant_type varchar(250) PRIMARY KEY NOT NULL,
    -> price decimal(6,2) NOT NULL
    -> );

CREATE TABLE plantinfo (
    -> name varchar(250) PRIMARY KEY NOT NULL,
    -> scientific_name varchar(250),
    -> light_needs varchar(250),
    -> water_needs varchar(250),
    -> plant_type varchar(250) NOT NULL,
    -> stock int DEFAULT 0,
    -> FOREIGN KEY (plant_type) REFERENCES plantprices(plant_type)
    -> );