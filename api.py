from flask import Flask, request, Response, jsonify
from mongoConnection import *
from bson import json_util, ObjectId
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson import json_util


app = Flask("harrypotterapi")

# Endpoints

#Bienvenid@ a la API!

@app.route("/welcome") 
def welcome():
    return "Welcome to the magical world of Harry Potter"

# Mostrar todos los quotes;

@app.route("/phrase") 
def list_phrases():
    qts = get_quotes()
    return jsonify(qts)

# Mostrar un quote;

@app.route("/phrase/<phrase>") 
def list_one_phrase(phrase):
    qo = get_one_quote(phrase)
    return jsonify(qo)   

# Mostrar todos los persoanajes;    

@app.route("/characters") 
def list_characters():
    ch = get_characters()
    return jsonify(ch)

# Mostrar un persoanaje;   

@app.route("/characters/<character>") 
def list_one_char(character):
    co = get_one_char(character)
    return jsonify(co)  

# Mostrar todas las peliculas;  

@app.route("/movies") 
def list_movies():
    mv = get_movies()
    return jsonify(mv)

# Mostrar una pelicula; 

@app.route("/movies/<movie>") 

def list_one_movie(movie):
    mo = get_one_movie(movie)
    return jsonify(mo)

# Insertar un quote;

@app.route("/add/new_quote/<Characters>/<Phrase>/<Movie>/<Year>") #FUNCIONA!
def add_new_quote(Characters, Phrase, Movie, Year):
    res = get_one_quote(Phrase)
    if len(res) > 0:
        return "The quote already exists"
    else:
        insert_quote(Characters, Phrase, Movie, Year)
        return "The new quote has been added correctly"

# Insertar un personaje;

@app.route("/add/new_char/<Characters>/<Role>/<Actorname>") 
def add_new_char(Characters, Role, Actorname):
    res = get_one_char(Characters) 
    if len(res) > 0:
        return "The character already exists"
    else:
        insert_char(Characters, Role, Actorname)
        return "The character has been added correctly"


# Eliminar un quote;

@app.route("/delete_quote/<Characters>/<Phrase>/<Movie>/<Year>") 
def delete_quotes(Characters, Phrase, Movie, Year):
    res = get_one_quote(Phrase)
    if len(res) > 0:
        delete_quote(Characters, Phrase, Movie, Year)
        return "The quote has been deleted correctly"
    else:
        return "The quote you want to delete does not exist"


# Eliminar un personaje; 

@app.route("/delete_char/<Characters>/<Role>/<Actorname>") 
def delete_chars(Characters, Role, Actorname):
    res = get_one_char(Characters)
    if len(res) > 0:
        delete_char(Characters, Role, Actorname)
        return "The quote has been deleted correctly"
    else:
        return "The quote you want to delete does not exist"


app.run(debug=True)