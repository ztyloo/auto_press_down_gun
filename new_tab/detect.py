import os
import time
import cv2
import numpy as np
import yaml

from utils import get_screen
from new_tab.detectors import *
from new_tab.tab_utils import get_pos_im

class Tab:
    def __init__(self):
        with open('new_tab/tab_position.yaml') as yml_file:
            self.yml = yaml.load(yml_file)

        self.in_tab_detector = In_Tab_Detector()
        self.gun_detector = Gun_Name_Detector()
        self.scope_detector = Scope_Name_Detector()
        self.hm_detector = Helmet_Name_Detector()
        self.bp_detector = Backpack_Name_Detector()
        self.vt_detector = Vest_Name_Detector()

    def detect(self, screen):
        is_in_tab_im = get_pos_im(self.yml, screen, 'is_in_tab')
        is_in_tab = self.in_tab_detector.detect(is_in_tab_im)

        gun1_im = get_pos_im(self.yml, screen, 'weapon')
        gun1 = self.gun_detector.detect(gun1_im)
        scope1_im = get_pos_im(self.yml, screen, 'scope')
        scope1 = self.scope_detector.detect(scope1_im)

        gun2_im = get_pos_im(self.yml, screen, '_weapon')
        gun2 = self.gun_detector.detect(gun2_im)
        scope2_im = get_pos_im(self.yml, screen, '_scope')
        scope2 = self.scope_detector.detect(scope2_im)

        hm_im = get_pos_im(self.yml, screen, 'helmet')
        hm = self.hm_detector.detect(hm_im)

        bp_im = get_pos_im(self.yml, screen, 'backpack')
        bp = self.bp_detector.detect(bp_im)

        vt_im = get_pos_im(self.yml, screen, 'vest')
        vt = self.vt_detector.detect(vt_im)







if __name__ == '__main__':
    pass