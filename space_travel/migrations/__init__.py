import random
import datetime
from pymongo import MongoClient
from space_travel.helpers import planet_name_generate, resource_name_generate

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
    collection.insert_one({"id": 1, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 2, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 3, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 4, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 5, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 6, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 7, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 8, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 9, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 10, "name": planet_name_generate(), "created_at": datetime.datetime.now(), "disabled_at": None})

    # creating or switching to space_travel_resource
    collection = db.space_travel_resource

    # Inserting documents
    collection.insert_one({"id": 1, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 2, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 3, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 4, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 5, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 6, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 7, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 8, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 9, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
    collection.insert_one({"id": 10, "name": resource_name_generate(), "weight": random.randint(1,100), "created_at": datetime.datetime.now(), "disabled_at": None})
