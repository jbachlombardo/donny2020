from apscheduler.schedulers.blocking import BlockingScheduler
import runpy

scheduler = BlockingScheduler()

def donny_job() :
    runpy.run_path('donny2020.py')

scheduler.add_job(donny_job, 'interval', hours = 1, start_date='2020-03-13 12:00:00')

scheduler.start()
