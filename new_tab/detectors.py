
from utils import Detection
from lists import *


png_dir = 'new_tab/pngs'

class Gun_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = gun_name_list
        super()._fill_png_dict()


class Scope_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = scope_name_list
        super()._fill_png_dict()


class Helmet_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = helmet_name_list
        super()._fill_png_dict()


class Backpack_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = backpack_name_list
        super()._fill_png_dict()


class Vest_Name_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = vest_name_list
        super()._fill_png_dict()


class In_Tab_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = in_tab_list
        super()._fill_png_dict()


class Ground_Back_Detector(Detection):
    def __init__(self):
        super().__init__()
        self.png_dir = png_dir
        self.item_list = in_tab_list
        super()._fill_png_dict()
