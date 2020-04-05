from Sibyl_System import Sibyl_logs, ENFORCERS, ACCEPTORS, Sibyl_approved_logs
from Sibyl_System.strings import scan_request_string, scan_approved_string
from Sibyl_System import Sibyl
from telethon import events
import re
import asyncio

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!/]scan'))
async def scan(event):
    if event.from_id in ENFORCERS and event.reply:
          replied = await event.get_reply_message() 
          if replied.fwd_from: 
             reply = replied.fwd_from
             if reply.from_id in ENFORCERS or reply.from_id in ACCEPTORS:
                   return
             if reply.from_name: 
                 sender = f"[{reply.from_name}](tg://user?id={reply.from_id})"
             else: 
                 sender = f"{reply.from_id}"
          else: 
                 if replied.sender.id in ACCEPTORS or replied.sender.id in ENFORCERS:
                          return
                 sender = f"[{replied.sender.first_name}](tg://user?id={replied.sender.id})"
          executer = await event.get_sender()
          try:
             reason = event.text.split(" ", maxsplit = 1)[1]
          except:
             return
          if replied.video or replied.document or replied.contact or replied.gif or replied.media or replied.sticker:
               await replied.forward_to(Sibyl_logs)
          await Sibyl.send_message(Sibyl_logs, scan_request_string.format(enforcer=f"[{executer.first_name}](tg://user?id={executer.id})", spammer=sender, message = replied.text, reason= reason))
    else:
     return

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!/]approve'))
async def approve(event):
 if event.from_id in ACCEPTORS and event.reply:
     replied = await event.get_reply_message()
     reply = replied.sender.id
     me = await Sibyl.get_me()
     sender = await event.get_sender()
     if reply == me.id:
            list = re.findall('tg://user\?id=(\d+)', replied.text)
            reason = re.search(r"Reason: (.*)", replied.text).group(1)
            if len(list) > 1:
               id1 = list[0]
               id2 = list[1]
            else:
               id1 = list[0]
               id2 = re.findall('(\d+)', replied.text)[1]
            if id1 in ENFORCERS or ACCEPTORS: 
                enforcer = id1
                scam = id2
            else:
                enforcer = id2
                scam = id1
            await Sibyl.send_message(Sibyl_approved_logs, scan_approved_string.format(enforcer=enforcer, scam=scam, approved_by= f"[{sender.first_name}](tg://user?id={sender.id})"))
            await Sibyl.send_message(Sibyl_logs, f"/gban [{scam}](tg://user?id={scam}) {reason} // By {enforcer} | #{replied.id}") 

@Sibyl.on(events.NewMessage(pattern=r'[\.\?!/]proof'))
async def proof(event): 
  if event.from_id in ACCEPTORS:
     msg = await Sibyl.send_message(event.chat_id, 'Trying to get Proof owo >>>>>')
     try: 
       proof_id = int(event.text.split(' ', 1)[1])
     except:
        await msg.edit('>>>>> Proof id is not valid') 
        return
     await msg.edit('Fetching msg details from proof id <<<<<<<') 
     proof = await Sibyl.get_messages(Sibyl_logs, ids=proof_id)
     reason = re.search(r"Reason: (.*)", proof.message).group(1)
     try:
         message = re.search('Message: (.*)', proof.message, re.DOTALL).group(1)
     except:
       if message and message == "":
            proof_id -= 1
            proof = await Sibyl.get_messages(Sibyl_logs, ids=proof_id)
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
            
@Sibyl.on(events.NewMessage(pattern=r'[\.\?!/]reject'))
async def proof(event):
  if event.from_id in ACCEPTORS and event.reply:
      replied = await event.get_reply_message()
      id = replied.id
      await Sibyl.edit_message(Sibyl_logs, id, reject_string, file = "https://anonymousfiles.io/f/04d280a88d8e6376912854c5900e3d641a848b48_hq.gif.mp4", force_document = True)

help_plus ="""
Here is the help for **Main**:

`scan` - Reply to a message with reason to send a request for gbans
`approve` - Approve a scan request
`proof` - Get message from proof id which is at the end of gban msg 
"""

__plugin_name__ = "Main" 
