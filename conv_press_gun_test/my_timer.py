import time
import threading
from threading import Timer, Thread, Event
from apscheduler.schedulers.background import BackgroundScheduler

import time


class MyTimer():
    def __init__(self, t_interval, hFunction, times):
        # self.stop_flag = False
        self.times = times
        self.counter =0
        self.t = t_interval
        self.hFunction = hFunction
        self.scheduler = BackgroundScheduler()
        self.timer_job = self.scheduler.add_job(self.hFunction, 'interval', seconds=self.t)
        self.scheduler.start()
        self.timer_job.pause()

    def reset(self):
        self.counter = 0

    def start(self):
        self.timer_job.resume()


    def cancel(self):
        self.timer_job.pause()


if __name__ == '__main__':
    def print_func():
        print(11111)

    tm = MyTimer(0.1, print_func)
    tm.start()