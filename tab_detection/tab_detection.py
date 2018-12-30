import os
import time
import cv2
import numpy as np
import yaml

from utils import get_screen
from tab_detection.detectors import *
from tab_detection.tab_utils import get_pos_im


class Tab_Detector:
    def __init__(self, state):
        with open('tab_detection/tab_position.yaml') as yml_file:
            self.yml = yaml.load(yml_file)

        self.state = state

        self.in_tab_detector = In_Tab_Detector()
        self.gun_detector = Gun_Name_Detector()
        self.scope_detector = Scope_Name_Detector()
        self.hm_detector = Helmet_Name_Detector()
        self.bp_detector = Backpack_Name_Detector()
        self.vt_detector = Vest_Name_Detector()

    def detect(self, screen):
        is_in_tab_im = get_pos_im(self.yml, screen, 'is_in_tab')
        self.state.is_in_tab = self.in_tab_detector.detect(is_in_tab_im)

        gun1_im = get_pos_im(self.yml, screen, 'weapon1')
        self.state.gun1 = self.gun_detector.detect(gun1_im)
        scope1_im = get_pos_im(self.yml, screen, 'scope1')
        scope1 = self.scope_detector.detect(scope1_im)
        self.state.scope1 = 1 if scope1 is None else int(scope1[1])

        gun2_im = get_pos_im(self.yml, screen, 'weapon2')
        self.state.gun2 = self.gun_detector.detect(gun2_im)
        scope2_im = get_pos_im(self.yml, screen, 'scope2')
        scope2 = self.scope_detector.detect(scope2_im)
        self.state.scope2 = 1 if scope2 is None else int(scope2[1])

        hm_im = get_pos_im(self.yml, screen, 'helmet')
        self.state.hm = self.hm_detector.detect(hm_im)
        bp_im = get_pos_im(self.yml, screen, 'backpack')
        self.state.bp = self.bp_detector.detect(bp_im)
        vt_im = get_pos_im(self.yml, screen, 'vest')
        self.state.vt = self.vt_detector.detect(vt_im)

        print('gun1:'+str(self.state.gun1)+'gun2:'+str(self.state.gun2))


if __name__ == '__main__':
    pass