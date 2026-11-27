from datetime import datetime, timedelta
from collections import defaultdict, deque
import ipaddress

LOG_FILE = "/var/log/auth.log"
teste = "Nov 19 10:23:51 server sshd[1234]: Failed password for from from 203.0.113.5 port 52817 ssh2"

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

    try: 
        invert = partes[::-1]
        i = invert.index("from")
        pos_from = len(partes) - 1 - i
        ip = partes[pos_from + 1]

        ipaddress.ip_address(ip)
        pos_for = partes.index("for")
    except (ValueError, IndexError):
        return None

    middle = partes[pos_for + 1 : pos_from]

    if middle[:2] == ["invalid", "user"]:
        valid_user = False
        user_words = middle[2:]
    else:
        valid_user = True
        user_words = middle

    if not user_words:
        return None
    
    user = " ".join(user_words)

    # TODO: build timestemp with datetime.strtime

    return {"timestamp": None, "status": status, "valid user": valid_user, "user": user, "ip": ip}
    

print(parse_line(teste))