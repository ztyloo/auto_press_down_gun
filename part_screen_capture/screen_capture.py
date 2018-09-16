import os
import time
import cv2
import numpy as np
from PIL import ImageGrab
import itchat


shield = cv2.imread('part_screen_capture/shield.png')
shield = shield / 255.0

origin = cv2.imread('part_screen_capture/origin.png')
# itchat.login()
if len(os.listdir('cap')) == 0:
    i = 0
else:
    i = max(os.listdir('cap'), key=lambda x: int(x[:-4]))
    i = int(i[:-4])

while True:

    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    ryanshuai_grab = screen[46:81, 1620:1818, :]

    if np.sum(abs(ryanshuai_grab-origin) * shield) < 10:
        # itchat.send('is Ryanshuai   ' + str(i), 'filehelper')
        print('is Ryanshuai   ' + str(i))
        cv2.imwrite('cap/'+str(i)+'.png', screen)
        i = i + 1
        time.sleep(10)

