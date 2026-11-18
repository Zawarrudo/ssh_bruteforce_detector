import time
import re
from collections import defaultdict

LOG_FILE = "/var/log/auth.log"

MAX_ATTEMPTS = 5
TIME_WINDOW = 60

