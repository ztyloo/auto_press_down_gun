import time
import threading
from threading import Timer, Thread, Event
from apscheduler.schedulers.blocking import BlockingScheduler


# class MyTimer():
#     def __init__(self, t_interval, hFunction):
#         # self.stop_flag = False
#         self.t = t_interval
#         self.hFunction = hFunction
#         self.scheduler = BlockingScheduler()
#         self.job = self.scheduler.add_job(self.hFunction, 'interval', seconds=self.t)
#
#     def start(self):
#         self.scheduler.start()
#
#     def cancel(self):
#         self.scheduler.shotdown(wait=True | False)


class MyTimer():
    def __init__(self,t,hFunction, max_x):
        # self.stop_flag = False
        self.t = t
        self.x = 0
        self.max_x = max_x
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)

    def handle_function(self):
        if not self.x == self.max_x:
            self.x += 1
            self.hFunction()
            self.thread = Timer(self.t,self.handle_function)
            self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


# class MyTimer(Thread):
#     """Call a function after a specified number of seconds:
#
#             t = Timer(30.0, f, args=None, kwargs=None)
#             t.start()
#             t.cancel()     # stop the timer's action if it's still waiting
#
#     """
#
#     def __init__(self, interval, function, args=None, kwargs=None):
#         Thread.__init__(self)
#         self.interval = interval
#         self.function = function
#         self.args = args if args is not None else []
#         self.kwargs = kwargs if kwargs is not None else {}
#         self.finished = Event()
#
#     def cancel(self):
#         """Stop the timer if it hasn't finished yet."""
#         print('in cancel')
#         self.finished.set()
#         print('out cancel')
#
#     def run(self):
#         while not self._is_stopped:
#             self.finished.wait(self.interval)
#             if not self.finished.is_set():
#                 self.function(*self.args, **self.kwargs)
#
#         self.finished.set()


#
# class MyTimer(threading.Thread):
#     def __init__(self, t_interval, hFunction, max_x):
#         threading.Thread.__init__(self)
#         self.event = threading.Event()
#         self.t = t_interval
#         self.hFunction = hFunction
#         self.count = max_x
#
#     def run(self):
#         while self.count > 0 and not self.event.is_set():
#             self.hFunction()
#             self.count -= 1
#             self.event.wait(self.t)
#
#     def stop(self):
#         self.event.set()
#

if __name__ == '__main__':
    def print_func():
        print(11111)

    tm = MyTimer(0.1, print_func, 10)
    tm.start()