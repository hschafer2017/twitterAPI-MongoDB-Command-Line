from pymongo import MongoClient
import os

MONGODB_URI = os.environ.get('MONGODB_URI')
MONGODB_NAME = os.environ.get('MONGODB_NAME')

buster = {
    'breed': 'sheltie',
    'color': 'white',
    'age': 4, 
    'gender': 'male'
}

with MongoClient(MONGODB_URI) as conn:
    db = conn[MONGODB_NAME]
    d = db['dogs']
    c = db['cats']
    b = db['Dogs']
    d.insert(buster)