import requests
import json
from xlwt import *

url = "https://pokeapi.co/api/v2/pokemon/"

# Getting data from the pokemon section of the API
response = requests.get(url)
data = response.json()

# Extracting the count from the url (well over 1000) took way too long so I decided to use 1st gen pokemon only - the first 151
poke_count =  151 

# List to contain extracted below for each pokemon
poke_data = []

num = 1
# Loop through each url and extract data
while num <= poke_count:
    poke_url = url + str(num) # url for each pokemon
    data = requests.get(poke_url).json() # get json of reports for each page
    
    # Pokemon names
    name = data["name"]

    # Pokemon types
    types = []

    for item in data["types"]:
        types.append(item["type"]["name"])

    # Height and Weight
    height = data["height"]
    weight = data["weight"]

    # Abilities
    abilities = []

    for item in data["abilities"]:
        abilities.append(item["ability"]["name"])

    # Stats
    stats = []
    for item in data["stats"]:
        pd = {item["stat"]["name"]: item["base_stat"]}
        stats.append(pd)

    # Create dictionary containing above extradted data and add to the poke_data list
    poke_dict = {"name": name, "type": types, "height": height, "weight": weight, "abilities": abilities, "stats": stats}
    poke_data.append(poke_dict)

    num += 1



# Putting reports into a json file
filename = "pokemon.json"
f = open(filename, "w")
json.dump(poke_data, f, indent=4)



"""
url = "https://pokeapi.co/api/v2/pokemon/1"

# Getting data from the pokemon section of the API
response = requests.get(url)
data = response.json()


# Putting reports into a json file
filename = "pokemonexample.json"
f = open(filename, "w")
json.dump(data, f, indent=4)
"""
