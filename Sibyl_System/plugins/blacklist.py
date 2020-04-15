import pymongo 
from Sibyl_System import MONGO_CLIENT, System, SIBYL, ENFORCERS, Sibyl_logs
from telethon import events 
import asyncio 
import re 
db = MONGO_CLIENT['Sibyl']['Main']
#cant find better names
upd = {} 
owo = {}

def update_blacklist(word, add = False):
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

async def get_blacklist():
     json = db.find_one({'_id': 1})
     return json.get('blacklisted', []) 

@System.on(events.NewMessage(pattern=r'[\.\?!]addbl'))
async def addbl(event):
  if event.from_id in SIBYL:
     flag = re.match(".addbl -e (.*)", event.text, re.DOTALL)
     if flag:
        text = re.escape(flag.group(1))
     else:
       try:
         text = event.text.split(" ", 1)[1]
       except:
         return 
     a = update_blacklist(text, add = True)
     if a:
        await System.send_message(event.chat_id, f"Added {text} to blacklist") 
     else:
        await System.send_message(event.chat_id, f" {text} is already blacklisted") 

@System.on(events.NewMessage(pattern=r'[\.\?!]rmbl'))
async def rmbl(event):
  if event.from_id in SIBYL:
     try:
       text = event.text.split(" ", 1)[1]
     except:
       return 
     a = update_blacklist(text, add = False)
     if a:
        await System.send_message(event.chat_id, f"Removed {text} from blacklist") 
     else:
        await System.send_message(event.chat_id, f"{text} is not blacklisted") 

@System.on(events.NewMessage(pattern=r'[\.\?!]listbl'))
async def listbl(event):
   if event.from_id in SIBYL:
      list = await get_blacklist()
      msg = "Currently Blacklisted strings:\n"
      for x in list:
         msg += f"•{x}\n"
      await System.send_message(event.chat_id, msg) 

@System.on(events.MessageEdited(incoming=True))
@System.on(events.NewMessage(incoming=True))
async def auto_gban_request(event):
    if event.from_id in ENFORCERS or event.from_id in SIBYL:
         return
    text = event.text
    words = await get_blacklist()
    sender = await event.get_sender()
    if event.chat_id == Sibyl_logs: return 
    if words:
      for word in words:
          pattern = r"( |^|[^\w])" + word + r"( |$|[^\w])"
          if re.search(pattern, text, flags=re.IGNORECASE):
                  await System.send_message(Sibyl_logs, f"$AUTO\nTriggered by: [{event.from_id}](tg://user?id={event.from_id})\nMessage: {event.text}") 
__plugin_name__ ="blacklist" 


help_plus ="""
Here is help for **Blacklist**
`addbl` - Add trigger to blacklist 
Flags( -e // escape text ) 
format: "addbl -e xyz" & "addbl x.*y"
`rmbl` - remove trigger from blacklist 
format: "rmbl xyz"
`listbl` - list blacklisted words 
"""
