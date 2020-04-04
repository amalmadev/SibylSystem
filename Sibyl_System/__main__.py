from Sibyl_System.strings import help_string
from Sibyl_System import ACCEPTORS, Sibyl_logs, API_ID_KEY, API_HASH_KEY, STRING_SESSION, Sibyl
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

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!]status'))
async def status(event):
    if event.from_id in ACCEPTORS:
         await Sibyl.send_message(event.chat_id, on_string)
    else:
         return

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!]help'))
async def help(event):
    if event.from_id in ACCEPTORS:
         help_for = event.text.split(" ", 1)[1].lower()
         if help_for in HELP:
              await Sibyl.send_message(event.chat_id, HELP[help_for])
         else:
              return 
    else:
         return



Sibyl.start()
Sibyl.run_until_disconnected()
