from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

MONGO_URI = "mongodb+srv://jheisonx:426857jj@cluster0.aablucj.mongodb.net/?appName=Cluster0"
#MONGO_URI = "mongo"

#client = MongoClient(MONGO_URI, 27017)
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.get_database('book_db')