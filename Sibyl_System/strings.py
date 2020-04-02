on_string = "Sibyl-System Is on, We should die."
help_string = """
Here is the for Sibyl-System (All the cmd can be used with ?,!,.)
scan - send request for gban
status - check if bot is online
help - Peace. 
approve - Approve gban request
"""
scan_request_string = """
$SCAN
{enforcer} is scanning user {spammer}
Reason: {reason}
Message: {message} 
"""

scan_approved_string = """
$KILL
**Enforcer** = {enforcer}
**Scanned User** = {scam}
**Approved By** = {approved_by}
"""
