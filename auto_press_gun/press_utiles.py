import time
import threading
import win32api
import win32con
import pythoncom
import PyHook3 as pyHook


def mouse_down(y):
    try:
        x = 0
        y = int(y)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    except:
        print('Move Error')


class Mouse_listern(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.hm = pyHook.HookManager()

    def onMouseEvent(self, event):
        # 监听鼠标事件
        print("MessageName:", event.MessageName)
        print("Message:", event.Message)
        print("Time:", event.Time)
        print("Window:", event.Window)
        print("WindowName:", event.WindowName)
        print("Injected:", event.Injected)
        print("---")

        return True

    def run(self):
        self.hm.HookMouse()
        self.hm.MouseAll = self.onMouseEvent
        while True:
            pythoncom.PumpWaitingMessages()


if __name__ == '__main__':
    # i = 0
    # x, y = pag.position()
    # print(str(i) + ':', x, y)
    # while True:
    #     i += 1
    #     time.sleep(1)
    #     mouse_down(5 )
    #     x, y = pag.position()
    #     print(str(i) + ':', x, y)

    ml = Mouse_listern()
    ml.run()