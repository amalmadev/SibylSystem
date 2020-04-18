from telethon import events
import asyncio
import sys
import re
from Sibyl_System import system_cmd, System
from io import StringIO
import traceback

#Thanks to stackoverflow for existing https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement


@System.on(system_cmd(pattern = r"sibyl (exec|execute|x|ex)"))
async def run(event):
  code = event.text.split(" ", 2)
  if len(code) == 2: return
  stderr, output, wizardry = None, None, None
  code = code[2]
  old_stdout = sys.stdout
  old_stderr = sys.stderr
  redirected_output = sys.stdout = StringIO()
  redirected_error = sys.stderr = StringIO()
  try:
    await async_exec(code, event)
  except Exception:
    wizardry = traceback.format_exc()
  output = redirected_output.getvalue()
  stderr = redirected_error.getvalue()
  sys.stdout = old_stdout
  sys.stderr = old_stderr
  if wizardry: final = "**Output**:\n`" + wizardry
  elif output: final = "**Output**:\n`" + output
  elif stderr: final = "**Output**:\n`" + stderr
  else: final = "`OwO no output"
  await System.send_message(event.chat_id, final + '`' )


async def async_exec(code, event):
    exec(
        f'async def __async_exec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__async_exec'](event)


__plugin_name__ = "exec"

help_plus = """
Run code using **exec** 
CMD - <x or ex or exec or execute> your code here
EXAMPLE - `!x print("OWO")`
"""
