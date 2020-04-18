from Sibyl_System import MONGO_CLIENT
import pymongo
import asyncio

async def get_blacklist():
     json = db.find_one({'_id': 1})
     return json.get('blacklisted', []) 

async def update_blacklist(word, add = False):
     bl = db.find_one({'_id': 1})
     current = bl['blacklisted']
     if add:
        if word in current: 
             return False
        current.append(word)
     else:
        if word in current:
          current.remove(word)
        else: 
          return False
     upd['blacklisted'] = current
     owo['$set'] = upd
     db.update_one(db.find_one({'_id': 1}), owo)
     return True
