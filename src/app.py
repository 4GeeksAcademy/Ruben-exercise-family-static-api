"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
# from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# Create the jackson family object
jackson_family = FamilyStructure("Jackson")


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


# Generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Ruta que devuelve todos los miembros de la familia
@app.route('/members', methods=['GET'])
def handle_hello():
    members = jackson_family.get_all_members()
    response_body = {"family": members}
    return jsonify(response_body), 200


# Ruta que devuelve un solo miembro de la familia por su ID
@app.route('/members/<int:member_id>', methods=['GET'])
def handle_get_one_member(member_id):
    member = jackson_family.get_member(member_id)
    response_body = {"member": member}
    return jsonify(response_body), 200

# Ruta que añade un nuevo miembre a la familia
@app.route('/members', methods=['POST'])
def handle_add_new_member():
    new_member = request.get_json()
    jackson_family.add_member(new_member["first_name"], new_member["age"], new_member["lucky_numbers"])
    return jsonify({"message": "Usuario creado correctamente"}), 200

# Ruta que elimina un solo miembro de la familia por su ID
@app.route('/members/<int:member_id>', methods=['DELETE'])
def handle_delete_one_member(member_id):
    member = jackson_family.delete_member(member_id)
    response_body = {"member": member}
    if response_body["member"] is False:
        return jsonify(response_body), 404
    return jsonify(response_body), 200



# This only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
