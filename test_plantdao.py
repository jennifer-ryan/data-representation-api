from plant_dao import plantdao

# Test get all
"""
result = plantdao.getAll()
print(result)
"""

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

# Test update stock
"""
print("Original:")
result = plantdao.findByNameOrType("Prayer Plant")
print(result)
plantdao.updateStock("Prayer Plant", 12)
print("After update:")
result = plantdao.findByNameOrType("Prayer Plant")
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