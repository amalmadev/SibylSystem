from Sibyl_System import Sibyl_logs, ENFORCERS, SIBYL, Sibyl_approved_logs
from Sibyl_System.strings import scan_request_string, scan_approved_string
from Sibyl_System import System
from telethon import events
import re
import asyncio

def gban(enforcer, target, reason, msg_id, approved_by):
   await System.send_message(Sibyl_approved_logs, scan_approved_string.format(enforcer=enforcer, scam=target, approved_by= f"[{approved_by.first_name}](tg://user?id={approved_by.id})"))
   await System.send_message(Sibyl_logs, f"/gban [{target}](tg://user?id={target}) {reason} // By {enforcer} | #{msg_id}") 
   return True

@System.on(events.NewMessage(pattern=r'[\.\?!/]scan'))
async def scan(event):
    if event.from_id in ENFORCERS and event.reply:
          replied = await event.get_reply_message() 
          if replied.fwd_from: 
             reply = replied.fwd_from
             if reply.from_id in ENFORCERS or reply.from_id in SIBYL:
                   return
             if reply.from_name: 
                 sender = f"[{reply.from_name}](tg://user?id={reply.from_id})"
             else: 
                 sender = f"[{reply.from_id}](tg://user?id={reply.from_id})"
          else: 
                 if replied.sender.id in SIBYL or replied.sender.id in ENFORCERS:
                          return
                 sender = f"[{replied.sender.first_name}](tg://user?id={replied.sender.id})"
          executer = await event.get_sender()
          try:
             if re.match('-a', event.text) and executer.id in SIBYL:
                  reason = event.text.split(" ", 2)[2]
                  approve = True 
             else:
                  reason = event.text.split(" ", 1)[1]
                  approve = False
          except:
             return
          if replied.video or replied.document or replied.contact or replied.gif or replied.media or replied.sticker:
               await replied.forward_to(Sibyl_logs)
          await System.send_message(Sibyl_logs, scan_request_string.format(enforcer=f"[{executer.first_name}](tg://user?id={executer.id})", spammer=sender, message = replied.text, reason= reason))
    else:
     return

@System.on(events.NewMessage(pattern=r'[\.\?!/]approve'))
async def approve(event):
 if event.from_id in SIBYL and event.reply:
   replied = await event.get_reply_message()
   match = re.match('\$SCAN', replied.text)
   if match:
     reply = replied.sender.id
     me = await System.get_me()
     sender = await event.get_sender()
     if reply == me.id:
            list = re.findall('tg://user\?id=(\d+)', replied.text)
            reason = re.search(r"Scan Reason: (.*)", replied.text).group(1)
            if len(list) > 1:
               id1 = list[0]
               id2 = list[1]
            else:
               id1 = list[0]
               id2 = re.findall('(\d+)', replied.text)[1]
            if id1 in ENFORCERS or SIBYL: 
                enforcer = id1
                scam = id2
            else:
                enforcer = id2
                scam = id1
            gban(enforcer, scam, reason, replied.id, sender) 

@System.on(events.NewMessage(pattern=r'[\.\?!/]proof'))
async def proof(event): 
  if event.from_id in SIBYL:
     msg = await System.send_message(event.chat_id, 'Trying to get Proof owo >>>>>')
     try: 
       proof_id = int(event.text.split(' ', 1)[1])
     except:
        await msg.edit('>>>>> Proof id is not valid') 
        return
     await msg.edit('Fetching msg details from proof id <<<<<<<') 
     proof = await System.get_messages(Sibyl_logs, ids=proof_id)
     reason = re.search(r"Scan Reason: (.*)", proof.message).group(1)
     try:
         message = re.search('Target Message: (.*)', proof.message, re.DOTALL).group(1)
     except:
       if message and message == "":
            proof_id -= 1
            proof = await System.get_messages(Sibyl_logs, ids=proof_id)
            if proof:
             if proof.media:
                   proof.forward_to(event.chat_id)
             else:
                   await msg.edit(f"Error getting proof from id {proof_id}")
                   return
            else : 
                  await msg.edit(f" Failed to get proof, Is the proof id valid?")
                  return
     await msg.edit(f"**Proof from ID**[`{proof_id}`]:\n**Reason**: {reason}\n**Message**: `{message}`") 

reject_string ="""
$REJECTED
**Crime Coefficient**: `Under 100`

Suspect is not a target for enforcement action. The trigger of Dominator will be locked.
"""
            
@System.on(events.NewMessage(pattern=r'[\.\?!/]reject'))
async def proof(event):
  if event.from_id in SIBYL and event.reply:
   match = re.match('\$SCAN', event.text) 
   if match:
      replied = await event.get_reply_message()
      id = replied.id
      await System.edit_message(Sibyl_logs, id, reject_string)

help_plus ="""
Here is the help for **Main**:

`scan` - Reply to a message with reason to send a request for gbans
`approve` - Approve a scan request
`proof` - Get message from proof id which is at the end of gban msg 
"""

__plugin_name__ = "Main" 
