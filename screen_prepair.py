import time
import cv2
import numpy as np
from PIL import ImageGrab

i = 0
while True:
    i += 1
    print(i)
    screen = ImageGrab.grab()
    screen = np.array(screen)
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    cv2.imwrite('cap/'+str(i)+'.png', screen)

    time.sleep(1)

