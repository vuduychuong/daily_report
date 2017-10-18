import sys
import time

import schedule

from service import Request

sys.path.insert(0, '')

schedule.every(1).minutes.do(Request.getBalances)
while 1:
    schedule.run_pending()
    time.sleep(1)
