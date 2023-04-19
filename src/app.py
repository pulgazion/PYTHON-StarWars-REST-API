"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User , Character, Planet, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/characters', methods=['GET'])
def hande_characters():
    if request.method == 'GET':
        list_character = Character.query.all()
        character = []
        for item in list_character:
            character.append(item.serialize())
        return jsonify(character), 200

@app.route('/characters/<int:character_id>' , methods=['GET'])
def handnle_characters_by_id(character_id):
    if request.method == 'GET':
        planet = Planet.query.filter_by( id = character_id)
        get_character = []
        for item in user:
            get_character.append(item.serialize())
        if get_character == []:
            return jsonify({"error":"user not found"}), 400
        else:
            return jsonify(get_character), 200

@app.route('/planets', methods=['GET'])
def hande_planets():
    if request.method == 'GET':
        list_planets = Planet.query.all()
        planets = []
        for item in list_planets:
            planets.append(item.serialize())
        return jsonify(planets), 200

@app.route('/planets/<int:planet_id>' , methods=['GET'])
def handnle_planets_by_id(planet_id):
    if request.method == 'GET':
        planet = Planet.query.filter_by( id = planet_id)
        get_planet = []
        for item in user:
            get_planet.append(item.serialize())
        if get_planet == []:
            return jsonify({"error":"user not found"}), 400
        else:
            return jsonify(get_planet), 200







@app.route('/user', methods=['GET' ,'POST'])
def handnle_user():
    if request.method == 'GET':
        user_list = User.query.all()
        users =[]
        for item in user_list:
            users.append(item.serialize())
        return jsonify(users), 200
    if request.method == 'POST':
        data = request.json
        nuevo_user = User()
        nuevo_user.email = data['email']
        nuevo_user.password = data['password']
        db.session.add(nuevo_user)
        db.session.commit()
        return jsonify(data),201

@app.route('/user/<int:people_id>/favorites' , methods=['GET'])
def handnle_user_favorite_by_id(user_id):
    if request.method == 'GET':
        user_favorite = Favorite.query.filter_by( user_id = user_id)
        get_user_favorite = []
        for item in user_favorite:
            get_user_favorite.append(item.serialize())
        if get_user_favorite == []:
            return jsonify({"error":"user not found"}), 400
        else:
            return jsonify(get_user_favorite), 200





@app.route('/user/<int:people_id>/favorite/planet/<int:planet_id>', methods=['POST', 'DELETE'])
def handle_fav_by_planet_id(user_id, planet_id):
    if request.method == 'POST':
        data = resquet.json
        new_fav = Favorite()
        new_fav.user_id = user_id
        new_fav.fav = "planet"
        new_fav.fav_id = planet_id
        db.session.add(new_fav)
        db.session.commit()
        return jsonify(new_fav),201
    if request.method == 'DELETE':
        fav_planet_del = Favorite.query.filter_by(user_id =user_id,fav_id=planet_id, fav="planet" ).first()
        if fav_planet_del is None:
            return jsonify({
                    "Error": "Favorite planet not found"}), 400
        else:        
            db.session.delete(fav_planet_del)
            db.session.commit()
        return jsonify({
                    "Message": "Favorite planet deleted"}), 200
    

@app.route('/user/<int:people_id>/favorite/character/<int:character_id>', methods=['POST', 'DELETE'])
def handle_fav_by_character_id(user_id, character_id):
    if request.method == 'POST':
        data = resquet.json
        new_fav = Favorite()
        new_fav.user_id = user_id
        new_fav.fav = "character"
        new_fav.fav_id = character_id
        db.session.add(new_fav)
        db.session.commit()
        return jsonify(new_fav),201
    if request.method == 'DELETE':
        fav_character_del = Favorite.query.filter_by(user_id =user_id,fav_id=character_id, fav="character" ).first()
        if fav_character_del is None:
            return jsonify({
                    "Error": "Favorite planet not found"}), 400
        else:        
            db.session.delete(fav_character_del)
            db.session.commit()
        return jsonify({
                    "Message": "Favorite planet deleted"}), 200