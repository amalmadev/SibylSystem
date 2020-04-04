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
from Sibyl_System.plugins.whois import help_plus
from Sibyl_System.plugins.main_manager import help_plus as help_main
@Sibyl.on(events.NewMessage(pattern=r'[\.\?!]status'))
async def status(event):
    if event.from_id in ACCEPTORS:
         await Sibyl.send_message(event.chat_id, on_string)
    else:
         return

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!][Ss]ibyl help'))
async def help(event):
    if event.from_id in ACCEPTORS:
         await Sibyl.send_message(event.chat_id, help_plus + "\n" + help_main)
    else:
         return

from Sibyl_System.plugins import to_load
import Sibyl_System.plugins.whois
for load in to_load: importlib.import_module("Sibyl_System.plugins." + load)

Sibyl.start()
Sibyl.run_until_disconnected()
