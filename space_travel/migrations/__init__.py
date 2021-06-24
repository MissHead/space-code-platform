import datetime
from pymongo import MongoClient
from space_travel.helpers import planet_name_generate

def insertData(apps, schema_editor):
    # establing connection
    try:
        connect = MongoClient()
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    # connecting or switching to the database
    db = connect.space_database

    # creating or switching to space_travel_planet
    collection = db.space_travel_planet

    # Inserting documents
    planet1 = planet_name_generate()
    collection.insert_one({"id": 1, "name": planet1, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet2 = planet_name_generate()
    collection.insert_one({"id": 2, "name": planet2, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet3 = planet_name_generate()
    collection.insert_one({"id": 3, "name": planet3, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet4 = planet_name_generate()
    collection.insert_one({"id": 4, "name": planet4, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet5 = planet_name_generate()
    collection.insert_one({"id": 5, "name": planet5, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet6 = planet_name_generate()
    collection.insert_one({"id": 6, "name": planet6, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet7 = planet_name_generate()
    collection.insert_one({"id": 7, "name": planet7, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet8 = planet_name_generate()
    collection.insert_one({"id": 8, "name": planet8, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet9 = planet_name_generate()
    collection.insert_one({"id": 9, "name": planet9, "created_at": datetime.datetime.now(), "disabled_at": None})
    planet10 = planet_name_generate()
    collection.insert_one({"id": 10, "name": planet10, "created_at": datetime.datetime.now(), "disabled_at": None})
