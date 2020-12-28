from plant_dao import plantdao
"""
# Test get all
result = plantdao.getAll()
print(result)
"""
# Test get all plant types/prices
result = plantdao.getAllTypes()
print(result)

# Test find by name/type
"""
result = plantdao.findByNameOrType("flower")
print(result)
"""

# Test find by need
"""
result = plantdao.findByNeed("high", "medium")
print(result)
"""

# Test update price
"""
print("Original:")
result = plantdao.findByNameOrType("folia")
print(result)
plantdao.updatePrice("Foliage", 6.99)
print("After update:")
result = plantdao.findByNameOrType("folia")
print(result)
"""

# Test update plant
"""
plant2 = {
    "name":"Lucky Bambooooo",
    "scientific_name":"Dracaena sanderianaaaa",
    "light_needs":"Mediummmm",
    "water_needs":"Highhhh",
    "plant_type":"Foliage",
    "stock":333
}

print("Original:")
result = plantdao.findByNameOrType("Lucky")
print(result)
plantdao.updatePlant("Lucky Bamboo", plant2)
print("After update:")
result = plantdao.findByNameOrType("Lucky")
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
    "plant_type":"Foliage",
    "stock":3
}

plantdao.createPlant(plant)

result = plantdao.findByNameOrType("foliage")
print(result)
"""

# Test delete
"""
print("Original:")
result = plantdao.findByNameOrType("Foliage")
print(result)
plantdao.deletePlant("Lucky Bamboo")
print("After deletion:")
result = plantdao.findByNameOrType("Foliage")
print(result)
"""