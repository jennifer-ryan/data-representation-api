import mysql.connector as msql
import config 

class PlantDao:
    conn = ""

    # Set main sql command to global variable for use in functions
    global mainsql

    mainsql = """SELECT pi.name AS name, 
                pi.scientific_name AS scientific_name, 
                pi.light_needs AS light_needs, 
                pi.water_needs AS water_needs, 
                pi.plant_type AS plant_type, 
                pi.stock AS stock, 
                pp.price AS price 
                FROM plantinfo pi, plantprices pp 
                WHERE pi.plant_type=pp.plant_type"""

    # Estabish connection
    def __init__(self):
        self.conn =  msql.connect(
            host = config.mysql["host"],
            user = config.mysql["user"],
            password = config.mysql["password"],
            database = config.mysql["db"],
            auth_plugin='mysql_native_password'
        )

    # Get all data from both tables
    def getAll(self):
        cursor = self.conn.cursor()
        sql = mainsql
        cursor.execute(sql)
        results = cursor.fetchall()
        
        return_list = []
        
        for result in results:
            dict_result = self.convert_to_dict(result)
            return_list.append(dict_result)

        return return_list

        # Close the connection
        cursor.close()

    # Get all from just the plant prices table
    def getAllTypes(self):
        cursor = self.conn.cursor()
        sql = "SELECT  * from plantprices"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        return_list = []

        for result in results:
            colnames = ["plant_type", "price"]
            plant = {}

            for i, colname in enumerate(colnames):
                value = result[i]
                plant[colname] = value
            
            return_list.append(plant)

        return return_list
        # Close the connection
        cursor.close()

    # Find by name or type
    def findByNameOrType(self, name):
        cursor = self.conn.cursor()
        sql = mainsql + """ AND (pi.name LIKE %s
                OR pi.scientific_name LIKE %s
                OR pi.plant_type LIKE %s)"""
        
        value = "%" + name.title() + "%"
        values = [value, value, value]
        cursor.execute(sql, values)
        results = cursor.fetchall()
                
        return_list = []
        
        for result in results:
            dict_result = self.convert_to_dict(result)
            return_list.append(dict_result)

        return return_list

        # Close the connection
        cursor.close()


    # Find by plant needs
    def findByNeed(self, lightNeed, waterNeed):
        cursor = self.conn.cursor()
        sql = mainsql + """ AND pi.light_needs = %s
                AND pi.water_needs = %s
                """
        
        values = [lightNeed, waterNeed]
        cursor.execute(sql, values)
        results = cursor.fetchall()
                
        return_list = []
        
        for result in results:
            dict_result = self.convert_to_dict(result)
            return_list.append(dict_result)

        return return_list

        # Close the connection
        cursor.close()

    # Create entry
    def createPlant(self, plant):
        cursor = self.conn.cursor()
        sql = "INSERT INTO plantinfo (name, scientific_name, light_needs, water_needs, plant_type, stock) VALUES (%s, %s, %s, %s, %s, %s)"
        values = [
            plant["name"],
            plant["scientific_name"],
            plant["light_needs"],
            plant["water_needs"],
            plant["plant_type"],
            plant["stock"]
        ]

        # Execute command
        cursor.execute(sql, values)
        self.conn.commit()

        # Close the connection
        cursor.close()

    # Update plant prices
    def updatePrice(self, plant_type, price):
        cursor = self.conn.cursor()
        sql = "UPDATE plantprices SET price = %s WHERE plant_type = %s"
        values = [price, plant_type]
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    # Update plant stock
    def updatePlant(self, name, plant):
        cursor = self.conn.cursor()
        sql = """UPDATE plantinfo 
                SET name = %s, 
                scientific_name = %s, 
                light_needs = %s, 
                water_needs = %s, 
                plant_type = %s, 
                stock = %s
                WHERE name = %s 
                OR scientific_name = %s"""
        values = [
            plant["name"],
            plant["scientific_name"],
            plant["light_needs"],
            plant["water_needs"],
            plant["plant_type"],
            plant["stock"],
            name,
            name
        ]
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()

    # Delete plant
    def deletePlant(self, name):
        cursor = self.conn.cursor()
        sql = "DELETE FROM plantinfo WHERE name = %s OR scientific_name = %s"
        values = [name, name]
        cursor.execute(sql, values)
        self.conn.commit()
        cursor.close()


    # Convert tuples to dictionary objects
    def convert_to_dict(self, result):
        colnames = ["name", "scientific_name", "light_needs", "water_needs", "plant_type", "stock", "price"]
        plant = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                plant[colname] = value
        return plant

# Create instance of PlantDao
plantdao = PlantDao()