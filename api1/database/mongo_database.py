import json
import logging
import os

from pymongo import MongoClient

from api1.config.config import MONGO_DATABASE_NAME


class MongoDBConnection:
    _conn = None

    def __init__(self):
        mongo_credentials = {}
        if os.environ.get("LOCAL"):
            mongo_credentials = {
                "host": "mongo:27017",
                "username": "mongo",
                "password": "mongo",
            }
            MONGO_HOST = mongo_credentials["host"]
            MONGO_USERNAME = mongo_credentials["username"]
            MONGO_PASSWORD = mongo_credentials["password"]
            self.client = MongoClient(host=MONGO_HOST)

        else:
            MONGO_HOST = "mongo:27017"
            MONGO_USERNAME = "mongo"
            MONGO_PASSWORD = "mongo"
            self.client = MongoClient(host=MONGO_HOST)
        self.db = self.client[MONGO_DATABASE_NAME]

    @classmethod
    def conn(cls):
        if cls._conn is None:
            cls._conn = cls()
        return cls._conn

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def insert_one(self, collection, data):
        self.db[collection].insert_one(data)

    def insert(self, collection, data):
        self.db[collection].insert(data)

    def insert_many(self, collection, data):
        self.db[collection].insert_many(data)

    def find(self, collection, query, projection=None):
        return list(self.db[collection].find(query, projection=projection))

    def find_one(self, collection, query, projection=None):
        return self.db[collection].find_one(query, projection=projection)
