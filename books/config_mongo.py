from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

MONGO_URI = os.getenv('MONGO_URI')
if not MONGO_URI:
    raise ValueError('Mongo URI is not set in environment variables.')

#MONGO_URI = "mongo"

#client = MongoClient(MONGO_URI, 27017)
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.get_database('book_db')