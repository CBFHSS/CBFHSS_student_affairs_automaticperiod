import os
from apscheduler.schedulers.blocking import BlockingScheduler
import sys
import datetime
from datetime import date,datetime, timedelta
import time
import calendar
from services import push
if __name__ == '__main__': 
    service = BlockingScheduler() #Please set Timezone when run on Heroku
    service.add_job(push.push,'cron',day_of_week='mon-fri',hour=9,minute=0)
    try:
        service.start()
    except (KeyboardInterrupt, SystemExit):
        pass
