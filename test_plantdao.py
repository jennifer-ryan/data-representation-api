from plant_dao import plantdao

# Test get all
#result = plantdao.getAll()
#print(result)

# Test find by name/type
#result = plantdao.findByNameOrType("folia")
#print(result)

# Test find by need
#result = plantdao.findByNeed("high", "high")
#print(result)

# Test update price
"""result = plantdao.findByNameOrType("folia")
print(result)
plantdao.updatePrice("Foliage", 7.99)
result = plantdao.findByNameOrType("folia")
print(result)"""

# Test update stock
"""result = plantdao.findByNameOrType("Prayer Plant")
print(result)
plantdao.updateStock("Prayer Plant", 12)
result = plantdao.findByNameOrType("Prayer Plant")
print(result)"""


# Test delete
"""print("Original:")
result = plantdao.findByNameOrType("Foliage")
print(result)
plantdao.deletePlant("Lucky Bamboo")
print("After deletion:")
result = plantdao.findByNameOrType("Foliage")
print(result)
"""
# Creating new entry
"""
# Plant dictionary object
plant = {
    "name":"Lucky Bamboo",
    "scientific_name":"Dracaena sanderiana",
    "light_needs":"Medium",
    "water_needs":"High",
    "type":"Foliage",
    "stock":3
}
# Prints autoincremented number
returnvalue = plantdao.createPlant(plant)

print(returnvalue)
"""
