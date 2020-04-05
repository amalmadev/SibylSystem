
from Sibyl_System import SIBYL, Sibyl_logs, API_ID_KEY, API_HASH_KEY, STRING_SESSION, System
from Sibyl_System.strings import on_string
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging
import asyncio
import importlib

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

from Sibyl_System.plugins import to_load

HELP = {}
IMPORTED = {}
for load in to_load: 
    imported = importlib.import_module("Sibyl_System.plugins." + load)
    if not hasattr(imported, "__plugin_name__"):
        imported.__plugin_name__ = imported.__name__

    if not imported.__plugin_name__.lower() in IMPORTED:
        IMPORTED[imported.__plugin_name__.lower()] = imported

    if hasattr(imported, "help_plus") and imported.help_plus:
        HELP[imported.__plugin_name__.lower()] = imported 

@System.on(events.NewMessage(pattern=r'[\.\?!]status'))
async def status(event):
    if event.from_id in SIBYL:
         await System.send_message(event.chat_id, on_string)
    else:
         return

@System.on(events.NewMessage(pattern=r'[\.\?!]help'))
async def help(event):
    if event.from_id in SIBYL:
         help_for = event.text.split(" ", 1)[1].lower()
         if help_for in HELP:
              await System.send_message(event.chat_id, HELP[help_for].help_plus)
         else:
              return 
    else:
         return



System.start()
System.run_until_disconnected()
