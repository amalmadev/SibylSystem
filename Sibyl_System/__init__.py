from telethon import TelegramClient, events
import asyncio
import aiohttp
from telethon.sessions import StringSession
import os
import pymongo
import re 


ENV = bool(os.environ.get('ENV', False))
if ENV:
   API_ID_KEY = int(os.environ.get('API_ID_KEY', None))
   API_HASH_KEY = os.environ.get('API_HASH_KEY', None)
   STRING_SESSION = os.environ.get('STRING_SESSION', None)
   SIBYL = list(int(x) for x in os.environ.get("SIBYL", "").split())
   ENFORCERS = list(int(x) for x in os.environ.get("ENFORCERS", "").split())
   MONGO_DB_URL = os.environ.get('MONGO_DB_URL') 
   Sibyl_logs = int(os.environ.get('Sibyl_logs', None))
   Sibyl_approved_logs = int(os.environ.get('Sibyl_Approved_Logs', None))
   GBAN_MSG_LOGS = int(os.environ.get('GBAN_MSG_LOGS', None)) 
else:
 import Sibyl_System.config
 API_ID_KEY = config.API_ID 
 API_HASH_KEY = config.API_HASH 
 STRING_SESSION = config.STRING_SESSION
 MONGO_DB_URL = config.MONGO_DB_URL
 SIBYL = config.SIBYL
 ENFORCERS = config.ENFORCERS
 Sibyl_logs = config.Sibyl_logs
 Sibyl_approved_logs = config.Sibyl_approved_logs
 GBAN_MSG_LOGS = config.GBAN_MSG_LOGS

ENFORCERS.extend(SIBYL)
session = aiohttp.ClientSession()
System = TelegramClient(StringSession(STRING_SESSION), API_ID_KEY, API_HASH_KEY)
MONGO_CLIENT = pymongo.MongoClient(MONGO_DB_URL)
collection = MONGO_CLIENT['Sibyl']['Main'] 
if collection.count_documents({ '_id': 1}, limit = 1) == 0:
   dict = {"_id": 1}
   dict["blacklisted"] = []
   collection.insert_one(dict) 

if collection.count_documents({ '_id': 2}, limit = 1) == 0:
   dict = {"_id": 2, "Type": "Wlc Blacklist"}
   dict["blacklisted_wlc"] = []
   collection.insert_one(dict)

def system_cmd(pattern=None, allow_sibyl=True, allow_enforcer = False, **args):
    if pattern:
        args["pattern"] = re.compile(r"[\?\.!/]" + pattern)
    if allow_sibyl and allow_enforcer:
        args["from_users"] = ENFORCERS
    else:
        args["from_users"] = SIBYL
    return events.NewMessage(**args)
