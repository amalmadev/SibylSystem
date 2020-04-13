import pymongo 
from Sibyl_System import MONGO_CLIENT, System, SIBYL, ENFORCERS

db = MONGO_CLIENT['Sibyl']['Main']
#cant find better names
upd = {} 
owo = {}
def add_to_blacklist(word):
     bl = db.find_one({'_id': 1})
     current = bl['blacklisted']
     current.append(word)
     upd['blacklisted'] = current
     owo['$set'] = upd
     db.update_one(with, bl)
