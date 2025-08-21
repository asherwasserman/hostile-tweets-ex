import os
from pymongo import MongoClient
import pandas as pd

class Dal:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri, tls=True)
        self.db = self.client[db_name]
        self.collections = self.db.list_collection_names()
        self.coll = self.db[self.collections[0]]

    def get_all_data(self):
        return list(self.coll.find({},{}))

