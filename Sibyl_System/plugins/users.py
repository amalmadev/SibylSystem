from Sibyl_System import SIBYL, ENFORCERS
from Sibyl_System import System
import asyncio
from telethon import events

@System.on(events.NewMessage(pattern=r'[\.\?!/]addenf'))
async def addenf(event):
  if event.from_id in SIBYL:
     if event.reply:
        replied = await event.get_reply_message()
        id = reply.from_id
     else:
        id = event.text.split(" ", 2)[1]
     if id in ENFORCERS:
           await System.send_message(event.chat_id, 'That person is already Enforcer!')
           return
     ENFORCERS.append(id)
     await System.send_message(event.chat_id, 'Done!) 
