on_string = "This chat is connected to Sibyl, Cymatic scans are now possible!"

#Make sure not to change this too much 
#If you still wanna change it change the regex too
scan_request_string = """
$SCAN
{enforcer} is requesting a Cymatic Scan for {spammer}
Scan Reason: {reason}
Target Message: {message} 
"""

scan_approved_string = """
#LethalEliminator
**Enforcer** = {enforcer}
**Target User** = {scam}
**Approved By** = {approved_by}
**Crime Coefficient**= Over 300
"""
# https://psychopass.fandom.com/wiki/Crime_Coefficient_(Index)
# https://psychopass.fandom.com/wiki/The_Dominator
