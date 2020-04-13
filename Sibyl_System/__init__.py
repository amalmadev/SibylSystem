from telethon import TelegramClient, events
import asyncio
import aiohttp
from telethon.sessions import StringSession
import os
import pymongo
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

ENFORCERS.extend(SIBYL)
session = aiohttp.ClientSession()
System = TelegramClient(StringSession(STRING_SESSION), API_ID_KEY, API_HASH_KEY)
MONGO_CLIENT = pymongo.MongoClient(MONGO_DB_URL)
