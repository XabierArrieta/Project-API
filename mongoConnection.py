from pymongo import MongoClient

client = MongoClient()

# 3 Collecciones

quots = client.harrypotter.quotes
chars = client.harrypotter.cast
movs = client.harrypotter.movies
db = client.harrypotter

# Funciones GET

# Función para obtener las quotes;

def get_quotes():
    query = {}
    project = {"_id":0,"Characters":1, "Phrase":1, "Movie":1,"Year":1}
    qt = (list(quots.find(query, project)))
    return qt

# Función para obtener una quote;

def get_one_quote(phrase):
    query = {"Phrase":str(phrase)}
    project = {"_id":0,}
    qo = (list(quots.find(query, project)))
    return qo

# Función para obtener los characters;

def get_characters():
    query = {}
    project = {"Characters":1, "_id":0, "Role":1, "Actor name":1}
    ch = (list(chars.find(query, project)))
    return ch

# Función para obtener un character;

def get_one_char(character):
    query = {"Characters":str(character)}
    project = { "_id":0}
    co = (list(chars.find(query, project)))
    return co

# Función para obtener las peliculas;

def get_movies():
    query = {}
    project = {"_id":0,"Movie":1,"Year":1,"Box office ( million $)":1}
    mv = (list(movs.find(query, project)))
    return mv

# Función para obtener una pelicula;

def get_one_movie(movie):
    query = {"Movie":str(movie)}
    project = {"_id":0}
    mo = (list(movs.find(query, project)))
    return mo

# Funciones POST

# Función para insertar un quote de un personaje;

def insert_quote(Characters, Phrase, Movie, Year):
    dic = {
        "Characters": f"{Characters}",
        "Phrase": f"{Phrase}",
        "Movie": f"{Movie}",
        "Year": f"{Year}"
    }
    insert = quots.insert_one(dic)
    return insert

# Función para insertar un personaje;

def insert_char(Characters, Role, Actorname):
    dic = {
        "Characters": f"{Characters}",
        "Role": f"{Role}",
        "Actor name": f"{Actorname}"
    }
    insert = chars.insert_one(dic)
    return insert

# Función para eliminar un quote;

def delete_quote(Characters, Phrase, Movie, Year):
    dic = {
        "Characters":f"{Characters}", 
        "Phrase":f"{Phrase}",  
        "Movie":f"{Movie}", 
        "Year":f"{Year}"
    }
    delete = quots.remove(dic)
    return delete

# Función para eliminar un personaje;
def delete_char(Characters, Role, Actorname):    
    dic = {
        "Characters": f"{Characters}",
        "Role": f"{Role}",
        "Actor name": f"{Actorname}"
        }
    delete = chars.remove(dic)
    return delete