# Data Representation API Project
This repository contains a Flask server API project as part of the assessment in the Data Representation and Querying module for the Higher Diploma in Data Analytics with Galway-Mayo Institute of Technology.

## About this Repository
The repository can be accessed [here](https://github.com/jennifer-ryan/data-representation-api). Clicking the 'clone or download' button will allow you to download the repository to your machine. Use the 'git clone' command followed by the repository link in your machine's command line to create a local copy for review. 

The contents of this repository are:

1. This **README** file that outlines the project.
2. A folder called **databasefiles** that contains files which can be used to recreate the database:
    - **createdb.sql** contains the commands used to initialise the database and tables.
    - **plant_info** and **plant_prices** CSV files contains the data used to fill the tables.
    - **make_tables.py** opens a connection to MySQL and populates the tables with the initial data.
3. A configuration template file **config_template.py** which contains the layout of the file used to connect to MySQL. The original config file has been placed in gitignore and so is not available.  
4. A Python file **plant_dao.py** which contains the functions that send CRUD operations to the MySQL database.
5. A Flask RESTful API, **rest_server.py** that uses HTTP requests to run the functions in plant_dao.py.
6. A folder called **staticpages** which contains the files for the webapp interface:
    - **login.html** contains a very simplistic, non-secure login page with username and password hardcoded.
    - **index.html** contains the API that runs from the server. 
    - An image file **plants.png** that is used in the login page.
7. A text file called **requirements.txt** which contains the packages required to run the API in a virtual environment. 
8. A text file called **serverlog.txt** which contains the logs of the server and gets updated every time the server run.

## Running the API
- You will need to have Python and my SQL already installed. 
- Open command line and clone the repository to your machine. 
- Open MySQL command line and use the files in the databasefiles folder to create the plantdb database, it's tables, and populate it with data from the CSV files.
- Back in your machine's command line, create a virtual environment and use requirements.txt to install the packages required using "pip install -r requirements.txt"
- Navigate into the virtual environment and run the command "python rest_server.py" The server is now running.
- Open local host in your browser.
- Log in using the username and password which can be seen by hovering over the text boxes.
- The API is now ready to use.   

## Navigating the API
The mySQL database contains two linked tables:
- plantinfo has the following data:
    - name
    - scientific name
    - light needs
    - water needs
    - plant type
    - stock
- plantprices has the following data:
    - plant type
    - price

The databases are linked on plant type which determines the price. 

Once the user has logged in, a table displaying all data from the database is called from the server. Each of these can be updated and deleted using the buttons beside each entry, which updates both the table and the database. Plant prices cannot be updated from this area as prices are linked to plant types. 

The Options button at the top of the page allows the user to:
- Search for plants by name, scientific name, or type. Partial searches are permitted.  
- Search for plants by needs - light and water - to suit their requirements.
- Create a new plant and add it to the database. Name and type are required entries but the rest of the information can be left blank if unknown and added at a later stage with the update button.
- Changes prices of plant types.
- Log out - return to the login page.   

## Browsers
Tested on Windows 10 64 bit OS with:
- Google Chrome Version 87.0.4280.88 (Official Build) (64-bit)
- Microsoft Edge Version 87.0.664.66 (Official build) (64-bit)
- Firefox Version 84.0.1 (64-bit)

## Deploying on Pythonanywhere
Unable to deploy on pythonanywhere. Will try another time http://jennyryan.pythonanywhere.com/