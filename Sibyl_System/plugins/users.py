from Sibyl_System import SIBYL, ENFORCERS
from Sibyl_System import System
import asyncio
from telethon import events

@System.on(events.NewMessage(pattern=r'[\.\?!/]addenf'))
async def addenf(event):
  if event.from_id in SIBYL:
     if event.reply:
        replied = await event.get_reply_message()
        id = replied.sender.id
     else:
        id = event.text.split(" ", 2)[1]
     if id in ENFORCERS:
           await System.send_message(event.chat_id, 'That person is already Enforcer!')
           return
     ENFORCERS.append(id)
     await System.send_message(event.chat_id, f'Added [{id}](tg://user?id={id}) to Enforcers') 

@System.on(events.NewMessage(pattern=r'[\.\?!/]rmenf'))
async def rmenf(event):
  if event.from_id in SIBYL:
     if event.reply:
        replied = await event.get_reply_message()
        id = replied.sender.id
     else:
        id = event.text.split(" ", 2)[1]
     if id in ENFORCERS:
           ENFORCERS.remove(id)
           await System.send_message(event.chat_id, f'Removed [{id}](tg://user?id={id}) from Enforcers') 
           return
     await System.send_message(event.chat_id, 'Is that person even a Enforcer?') 

@System.on(events.NewMessage(pattern=r'[\.\?!/]listusers'))
async def listuser(event):
  if event.from_id in SIBYL:
      msg = "Sibyl users:\n" 
      for x in SIBYL:
         try:
           user = await System.get_entity(x)
           msg += f"•[{user.first_name}](tg://user?id={user.id})\n"
         except:
           msg += f"•{x}\n"
      msg += "Enforcers:\n"
      for z in ENFORCERS:
         try:
           user = await System.get_entity(z)
           msg += f"•[{user.first_name}](tg://user?id={user.id})\n"
         except:
           msg += f"•{z}\n"
      await System.send_message(event.chat_id, msg)
