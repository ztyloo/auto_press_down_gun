import time
import win32api
import win32con
import pyautogui as pag

pag.moveRel()


if __name__ == '__main__':

    i = 0
    x, y = pag.position()
    print(str(i) + ':', x, y)
    while True:
        i += 1
        pag.moveRel(0, 50, 1)
        x, y = pag.position()
        print(str(i) + ':', x, y)

