import pymongo 
from Sibyl_System import MONGO_CLIENT, System, SIBYL, ENFORCERS

db = MONGO_CLIENT['Sibyl']['Main']
#cant find better names
upd = {} 
owo = {}
def add_to_blacklist(word):
     bl = db.find_one({'_id': 1})
     current = bl['blacklisted']
     current.append(word)
     upd['blacklisted'] = current
     owo['$set'] = upd
     db.update_one(owo, bl)

@System.on(events.NewMessage(pattern=r'[\.\?!]addbl'))
async def addenf(event):
  if event.from_id in SIBYL:
     try:
       text = event.text.split(" ", 1)[1]
     except:
       return 
     add_to_blacklist(text)
     await System.send_message(event.chat_id, f"Added {text} to blacklist") 
