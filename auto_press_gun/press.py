import threading
import pythoncom
import PyHook3 as pyHook


class Press(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._loop = True

    def set_states(self, all_states):
        pass

    def run(self):
        pass

    def stop(self):
        self._loop = False




if __name__ == '__main__':
    pl = Press()
    pl.run()
