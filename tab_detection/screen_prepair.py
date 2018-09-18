import os
import time
import cv2
import numpy as np
from PIL import ImageGrab


if len(os.listdir('../cap')) == 0:
    i = 0
else:
    i = max(os.listdir('../cap'), key=lambda x: int(x[:-4]))
    i = int(i[:-4])


while True:
    i += 1
    print(i)
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    cv2.imwrite('../cap/'+str(i)+'.png', screen)

    time.sleep(1)

