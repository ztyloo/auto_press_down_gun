import time
import cv2
import numpy as np
from PIL import ImageGrab
from pykeyboard import PyKeyboardEvent
from pymouse import PyMouseEvent


class Tab:
    def __init__(self):
        pass

    def screen_shot(self):
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        cv2.imwrite('state_image/' +  'now.png', screen)

    def
