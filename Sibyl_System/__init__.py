from telethon import TelegramClient, events
import asyncio

from telethon.sessions import StringSession
import os

ENV = bool(os.environ.get('ENV', False))
if ENV:
   API_ID_KEY = int(os.environ.get('API_ID_KEY', None))
   API_HASH_KEY = os.environ.get('API_HASH_KEY', None)
   STRING_SESSION = os.environ.get('STRING_SESSION', None)
   SIBYL = list(int(x) for x in os.environ.get("SIBYL", "").split())
   ENFORCERS = list(int(x) for x in os.environ.get("ENFORCERS", "").split())
   Sibyl_logs = int(os.environ.get('Sibyl_logs', None))
   Sibyl_approved_logs = int(os.environ.get('Sibyl_Approved_Logs', None))
else:
 import Sibyl_System.config
 API_ID_KEY = config.api_id
 API_HASH_KEY = config.api_hash
 STRING_SESSION = config.string_session
 SIBYL = config.SIBYL
 ENFORCERS = config.enforcers
 Sibyl_logs = config.Sibyl_logs
 Sibyl_approved_logs = config.Sibyl_approved_logs

ENFORCERS.extend(SIBYL)

Sibyl = TelegramClient(StringSession(STRING_SESSION), API_ID_KEY, API_HASH_KEY)
