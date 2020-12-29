# Data Representation API Project
This repository contains a Flask server API project as part of the assessment in the Data Representation and Querying module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

## About this Repository
The repository can be accessed [here](https://github.com/jennifer-ryan/data-representation-api). Clicking the 'clone or download' button will allow you to download the repository to your machine. Use the 'git clone' command followed by the repository link in your machine's command line to create a local copy for review.  

The contents of this repository are:

1. A **README** file that outlines the project.
2. A folder called **databasefiles** that contains the files that can be used to recreate the database:
    - **createdb.sql** contains the commands used to initialise the database and tables.
    - **plant_info** and **plant_prices** CSV files contains the data used to fill the tables.
    - **make_tables.py** opens a connection to MySQL and populates the tables with the initial data.
3. A configuration template file **config_template.py** which contains the layout of the config file used to connect to MySQL. The original config file has been placed in gitignore. 
4. A Python file **plant_dao.py** which contains functions that send CRUD operations to the MySQL database.
5. A Flask RESTful API, **rest_server.py** that uses HTTP requests to run the functions in plant_dao.py.
6. A folder called **staticpages** which contains the folders for the webapp interface:
    - **login.html** contains a very simple login page with username and password hardcoded.
    - **index.html** contains the API that runs the server. 
    - An image file **plants.png** that is used in the login page.
7. A text file called **requirements.txt** which contains the packages required to run the API.
8. A text file called **serverlog.txt** which contains the logs of the server and gets updated each time it's run.

## Navigating the API
The mySQL database contains two linked tables:
- plantinfo has the following data:
    - name
    - scientific name
    - light needs
    - water needs
    - plant type (link)
    - stock
- plantprices has the following data:
    - plant type (link)
    - price

Once the user has logged in, a table displaying all data from the database is called from the server. Each of these can be updated and deleted using the buttons beside each entry, which updates both the table and the database. Plant prices cannot be updated from this area as prices are linked to plant types. 

The Options button at the top of the page allows the user to:
- Search for plants by name, scientific name, or type. Partial searches are permitted.  
- Search for plants by needs - light and water - to suit their requirements.
- Create a new plant and add it to the database. Name and type are required entries but the rest of the information can be left blank if unknown and addes at a later stage with the update button.
- Changes prices of plant types.
- Log out - return to the login page.   

## Deploying on pythonanywhere
Attempting...