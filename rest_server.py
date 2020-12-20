from flask import Flask, url_for, request, redirect, abort, jsonify
from plant_dao import plantdao

app = Flask(__name__,
            static_url_path = "", 
            static_folder = "staticpages")

# Keep json objects sorted as in dictionary
app.config['JSON_SORT_KEYS'] = False

# Index
@app.route('/')
def index():
    return "Hello"
# curl http://127.0.0.1:5000

# Get all
@app.route('/plants')
def getAll():
    return jsonify(plantdao.getAll())
# curl http://127.0.0.1:5000/plants

# Find by name/type
@app.route('/plants/<string:name>')
def findByNameOrType(name):
    return jsonify(plantdao.findByNameOrType(name))
# curl http://127.0.0.1:5000/plants/name

# Create plant
@app.route('/plants', methods=['POST'])
def createPlant():
    if not request.json:
        abort(400)

    plant = {
        "name": request.json["name"],
        "scientific_name": request.json["scientific_name"],
        "light_needs": request.json["light_needs"],
        "water_needs": request.json["water_needs"],
        "plant_type": request.json["plant_type"],
        "stock": request.json["stock"]
    }

    return jsonify(plantdao.createPlant(plant))
# curl -X POST -d "{\"name\":\"test\", \"scientific_name\":\"science\", \"light_needs\":\"light\", \"water_needs\":\"water\", \"plant_type\":\"type\", \"stock\":5}" -H Content-Type:application/json http://127.0.0.1:5000/plants

# Update - not working yet
@app.route('/plants/<string:type>', methods=['PUT'])
def update(name):
    foundplant = plantdao.findByNameOrType(name)
    if foundplant == {}:
        return 404

    currentplant = foundplant
    if "price" in request.json:
        currentplant["price"] = request.json["price"]
        plantdao.updatePrice(currentplant)
    if "stock" in request.json:
        currentplant["stock"] = request.json["stock"]
        plantdao.updateStock(currentplant)

    return jsonify(currentplant)
# curl -X PUT -d "{\"stock\":5}" -H Content-Type:application/json http://127.0.0.1:5000/plants/type

# Delete
@app.route('/plants/<string:name>', methods=['DELETE'])
def delete(name):
    return jsonify({"done": True})
# curl -X DELETE http://127.0.0.1:5000/plants/name

if __name__ == "__main__":
    app.run(debug=True)

