from datetime import datetime, timedelta
from collections import defaultdict, deque

LOG_FILE = "/var/log/auth.log"
teste = "Nov 19 10:23:45 server sshd[1234]: Failed password for root from 203.0.113.5 port 52814 ssh2"

MAX_ATTEMPTS = 5
TIME_WINDOW = 60

def parse_line(line):
    if "sshd" not in line:
        return None
    
    if "Failed password" in line:
        status = "failed"
    elif "Accepted" in line:
        status = "accepted"
    else: 
        return None

    partes = line.split()

    # TODO: found IP using index "from"
    # TODO: found user name 
    # TODO: build timestemp with datetime.strtime

    return {"timestamp": None, "status": status, "user": None, "ip": None}

print(parse_line(teste))