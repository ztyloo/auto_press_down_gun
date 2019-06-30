import threading
import win32api
import win32con
import pythoncom
import PyHook3 as pyHook


class Press_Listener(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.hm = pyHook.HookManager()
        self.hm.MouseAll = self.onMouseEvent
        self._loop = True

    def set_state(self):
        pass

    def onMouseEvent(self, event):
        print("MessageName:", event.MessageName)
        print("Message:", event.Message)
        print("Time:", event.Time)
        print("Window:", event.Window)
        print("WindowName:", event.WindowName)
        print("Injected:", event.Injected)

        return True

    def run(self):
        self.hm.HookMouse()
        while self._loop:
            pythoncom.PumpWaitingMessages()

    def stop(self):
        self._loop = False


if __name__ == '__main__':
    pl = Press_Listener()
    pl.run()
