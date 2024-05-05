from flask import Flask, jsonify, request
from flask_cors import CORS

from back import *

app = Flask(__name__)
CORS(app)

users = []

@app.route("/users/", methods=['GET'])
def get_user():
    return jsonify(users)

@app.route("/user/", methods=['POST'])
def add_user():
    person = request.args.get("name")

    if person == None:
        return '', 400


    arrival_date = request.args.get("arrivalDate")

    if arrival_date == None:
        return '', 401

    return_date = request.args.get("departureDate")

    if return_date == None:
        return '', 402

    city_return = request.args.get("arrivalCity")

    if city_return == None:
        return '', 403

    city_arrival = request.args.get("departureCity")

    if city_arrival == None:
        return '', 404

    sport = request.args.get("selectSport")

    if sport == None:
        return '', 405

    """    users.append({
        "person": person,
        "arrival_date": arrival_date,
        "return_date": return_date,
        "arrival_city": city_arrival,
        "return_city": city_return,
        "sport": sport
        })
    """

    return str(insert_travel(person, arrival_date, return_date, city_arrival, city_return, sport)), 200

@app.route("/compatibility/", methods=['GET'])
def get_compatibility():
    trip_id = request.args.get("id")

    if trip_id == None:
        return '', 400

    # código

    user_data = get_user_data(trip_id)[0];

    print(user_data)

    compatibles = get_compatibles(trip_id, user_data[2], user_data[3], user_data[4], user_data[5], user_data[6]);

    country = countries[user_data[5]];

    compatibles = dict(compatibles)

    for key, values in compatibles.items():
        parsedDates = [parseDate(s) for s in values]
        compatibles[key] = parsedDates

    print(compatibles)

    resultado = obtener_personas_y_eventos(country, user_data[6], parseDate(user_data[2]), parseDate(user_data[3]), compatibles)

    pprint.pprint(resultado);

    return resultado, 200;
