from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

JWT_SECRET = os.environ.get('JWT_SECRET', '4z%3f*1m3)z9m$8q$1#7z@c_1e2+x#y$h&j@&k_ljjf#zj4_=w')
MONGO_URI = "mongodb+srv://jheisonx:426857jj@cluster0.aablucj.mongodb.net/?appName=Cluster0"
#MONGO_URI = "mongo"

#client = MongoClient(MONGO_URI, 27017)
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

db = client.get_database('book_db')