import os
import cv2

from utils import Detection

class Body_Pick(Detection):
    def __init__(self):
        super().__init__()
        self.helmet_list = ['helmet_lv3', 'helmet_lv2', 'helmet_lv1']
        self.vest_list = ['ves_lv3', 'ves_lv2', 'ves_lv1']
        self.backpack_list = ['backpack_lv3', 'backpack_lv2', 'backpack_lv1']
        self.item_list = self.helmet_list+self.vest_list+self.backpack_list

    def pick(self):
        