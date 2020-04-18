import pymongo 
from Sibyl_System import MONGO_CLIENT
import asyncio 
import re 
db = MONGO_CLIENT['Sibyl']['Main']
#cant find better names
upd = {} 
owo = {}


async def update_wlc_blacklist(word, add = False):
     db = MONGO_CLIENT['Sibyl']['Main']
     #cant find better names
     upd = {} 
     owo = {}
     bl = db.find_one({'_id': 2})
     current = bl['blacklisted_wlc']
     if add:
        if word in current: 
             return False
        current.append(word)
     else:
        if word in current:
          current.remove(word)
        else: 
          return False
     upd['blacklisted_wlc'] = current
     owo['$set'] = upd
     db.update_one(db.find_one({'_id': 2}), owo)
     return True


async def get_wlc_bl():
        db = MONGO_CLIENT['Sibyl']['Main']
        json = db.find_one({"_id": 2})
        return json.get("blacklisted_wlc", [])

