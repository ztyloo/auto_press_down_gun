import os
import time
import cv2
import numpy as np
from b_detection.fire_mode_detector import Fire_Mode_Detector
from all_state import State


class Tab_Detector:
    def __init__(self, state: State):
        self.state = state
        self.fire_mode_detector = Fire_Mode_Detector()

    def detect(self, screen):
        fire_mode_im = screen[1318: 1339, 1595: 1677, :]
        self.state.fire_mode1 = self.fire_mode_detector.detect(fire_mode_im)

