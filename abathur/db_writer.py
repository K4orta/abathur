import pymongo
from pymongo import MongoClient

def make_connection():
    client = MongoClient('localhost', 27017)
    db = client.blizzard
    col = db['matches']
    print(col.find_one())

if __name__ == '__main__':
    make_connection()