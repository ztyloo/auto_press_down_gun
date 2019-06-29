import numpy as np
import cv2
import os
from image_detect.crop_position import position


class Detector:
    def __init__(self, position_name, category_name):

        assert position_name in position
        crop_position = position[position_name]
        self.x0, self.x1, self.y0, self.y1 = crop_position['x0'], crop_position['x1'], crop_position['y0'], crop_position['y1']
        self.png_dict = dict()

        png_dir = os.path.join('D:/github_project/auto_press_down_gun/image_detect/states_4c_im', category_name)
        assert os.path.exists(png_dir)
        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def diff_sum_classify(self, screen, sum_thr=10000):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        for item_name, png in self.png_dict.items():
            if detect_item_sum(crop_im, png) < sum_thr:
                return item_name

    def water_mark_classify(self, screen, sum_thr=10000, c_thr=10):
        crop_im = screen[self.y0: self.y1, self.x0: self.x1, :]
        max_color = find_most_color(crop_im)

        crop_im_r = crop_im[:, :, 0] - max_color[0]
        crop_im_g = crop_im[:, :, 1] - max_color[1]
        crop_im_b = crop_im[:, :, 2] - max_color[2]
        shield_r = np.where(crop_im_r <= c_thr, 1, 0)
        shield_g = np.where(crop_im_g <= c_thr, 1, 0)
        shield_b = np.where(crop_im_b <= c_thr, 1, 0)

        shield = (shield_r*shield_g*shield_b).astype(np.uint8)

        # cv2.imshow('', shield*255)
        # cv2.waitKey()

        min_item = None
        min_sum = 1000000
        for item_name, png in self.png_dict.items():
            sum = detect_item_sum(crop_im, png)
            if sum < min_sum:
                min_item = item_name
                min_sum = sum
        return min_item

def detect_item_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray):
    test_im = detect_im_3c.copy()
    target_im = target_im_4c[:, :, 0:3]
    shield = target_im_4c[:, :, [3]]//255
    test_im = test_im * shield
    target_im = target_im * shield

    sum = np.sum(test_im - target_im)
    # print(sum)
    return sum


def find_most_color(im):
    color_num_dict = dict()
    for line in im:
        for x in line:
            color_num_dict[tuple(x)] = color_num_dict.get(tuple(x), 0)+1
    max_v = 0
    max_k = None
    for k,v in color_num_dict.items():
        if v > max_v:
            max_k = k
            max_v = v
    return max_k


if __name__ == '__main__':



    # screen = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/fire_mode/burst/burst.png')
    # # screen = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/fire_mode/full/full.png')
    # # screen = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/fire_mode/single/single.png')
    # fire_mode_detect = Detector('fire_mode', 'fire_mode')
    # a = fire_mode_detect.water_mark_classify(screen)
    # print(a)

    # screen = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/weapon/98k/98k.png')
    # fire_mode_detect = Detector('weapon', 'weapon')
    # a = fire_mode_detect.diff_sum_classify(screen)
    # print(a)

    import cv2
    import numpy as np
    from PIL import ImageGrab
    from pykeyboard import PyKeyboardEvent

    weapon_detect = Detector('weapon', 'weapon')
    class Key_listener(PyKeyboardEvent):
        def __init__(self):
            PyKeyboardEvent.__init__(self)
            self.i = 0

        def tap(self, keycode, character, press):

            if keycode == 162 and press:
                screen = ImageGrab.grab()
                screen = np.array(screen)
                screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
                a = weapon_detect.diff_sum_classify(screen)
                self.i += 1

        def escape(self, event):
            return False


    t = Key_listener()
    t.run()
