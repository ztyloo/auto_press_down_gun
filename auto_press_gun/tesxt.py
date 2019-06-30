import threading
import pyautogui as pag


if __name__ == '__main__':
    class TTTTT(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)

        def run(self):
            i = 0
            x, y = pag.position()
            print(str(i) + ':', x, y)
            while True:
                i += 1
                pag.moveTo(0, 50, 10)
                x, y = pag.position()
                print(str(i) + ':', x, y)

    tt = TTTTT()
    tt.run()




