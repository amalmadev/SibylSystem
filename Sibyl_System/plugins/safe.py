from Sibyl_System import System, system_cmd
from telethon import events
import asyncio
import os
import sys
import re

@System.on(system_cmd(pattern = r"sibyl restart"))
async def reboot(event):
    if event.fwd_from:
        return
    await System.disconnect()
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@System.on(system_cmd(pattern = r"sibyl shutdown"))
async def shutdown(event):
    if event.fwd_from:
        return
    await System.send_message(event.chat_id, "Shutting Down... ")
    await System.disconnect()
