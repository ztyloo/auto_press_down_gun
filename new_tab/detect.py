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
        yaml_path = 'tab_position.yaml'
        self.yml = yaml.load(open(yaml_path))
        self.gun_detector = Gun_Name_Detector()
        self.scope_detector = Scope_Name_Detector()
        self.hm_detector =

    def __del__(self):
        self.yml.close()

    def detect(self, screen):
        gun1_im = get_pos_im(self.yml, screen, 'weapon')
        gun2_im = get_pos_im(self.yml, screen, '_weapon')
        gun1 = self.gun_detector.detect(gun1_im)
        gun2 = self.gun_detector.detect(gun2_im)

        scope_im = get_pos_im(self.yml, screen, 'scope')
        scope = self.scope_detector.detect(scope_im)

        hm_im = get_pos_im(self.yml, screen, 'helmet')
        hm = self.scope_detector.detect(hm_im)

        bp_im = get_pos_im(self.yml, screen, 'backpack')
        bp = self.scope_detector.detect(bp_im)

        vt_im = get_pos_im(self.yml, screen, 'vest')
        vt = self.scope_detector.detect(vt_im)







if __name__ == '__main__':
    t = Tab()
    dir = 'pos_from/weapon'
    for im_name in os.listdir(dir):
        im_path = os.path.join(dir, im_name)
        t.now_screen = cv2.imread(im_path)

        t.test()

        # det = t.detect('user')
        # print(det)
        # det = t.detect('weapon')
        # print(det)
        # det = t.detect('scope')
        # print(det)
