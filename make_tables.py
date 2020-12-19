# Add contents of CSV files to the tables in the database

import csv
import mysql.connector as msql

# Establish connection
conn = msql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "plantdb"
)

# Creating a cursor object
cursor = conn.cursor()
"""
# Open CSV files
with open("plant_prices.csv") as pp:
    plantprices = csv.reader(pp, delimiter = ",")
    # Skip header information in csv
    next(plantprices)
    # Populate table with data from each row
    for row in plantprices:
        cursor.execute("INSERT INTO plantprices (type, price) VALUES (%s, %s)", row)
"""
with open("plant_info.csv") as pi:
    plantinfo = csv.reader(pi, delimiter = ",")
    # Skip header information in csv
    next(plantinfo)
    # Populate table with data from each row
    for row in plantinfo:
        cursor.execute("INSERT INTO plantinfo (id, name, scientific_name, light_needs, water_needs, type, stock) VALUES (%s, %s, %s, %s, %s, %s, %s)", row)  

# Commit changes to database
conn.commit()

# Close the connection
cursor.close()