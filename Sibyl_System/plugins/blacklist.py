import pymongo 
from Sibyl_System import MONGO_CLIENT, System, SIBYL, ENFORCERS
from telethon import events 

db = MONGO_CLIENT['Sibyl']['Main']
#cant find better names
upd = {} 
owo = {}

def add_to_blacklist(word, add = False):
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
     db.update_one(bl, owo)

@System.on(events.NewMessage(pattern=r'[\.\?!]addbl'))
async def addenf(event):
  if event.from_id in SIBYL:
     try:
       text = event.text.split(" ", 1)[1]
     except:
       return 
     a = add_to_blacklist(text, add = True)
     if a:
        await System.send_message(event.chat_id, f"Added {text} to blacklist") 
     else:
        await System.send_message(event.chat_id, f" {text} is already blacklisted") 

@System.on(events.NewMessage(pattern=r'[\.\?!]rmbl'))
async def addenf(event):
  if event.from_id in SIBYL:
     try:
       text = event.text.split(" ", 1)[1]
     except:
       return 
     a = add_to_blacklist(text, add = False)
     if a:
        await System.send_message(event.chat_id, f"Removed {text} from blacklist") 
     else:
        await System.send_message(event.chat_id, f" {text} is not blacklisted") 

