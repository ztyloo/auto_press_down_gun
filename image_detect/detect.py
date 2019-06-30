import numpy as np
import cv2
import os


class Detector:
    def __init__(self, category_name):
        self.png_dict = dict()

        png_dir = os.path.join('D:/github_project/auto_press_down_gun/image_detect/states_4c_im', category_name)
        assert os.path.exists(png_dir)
        for png_name in os.listdir(png_dir):
            abs_png_name = os.path.join(png_dir, png_name)
            png = cv2.imread(abs_png_name, cv2.IMREAD_UNCHANGED)
            self.png_dict[png_name[:-4]] = png

    def diff_sum_classify(self, crop_im, sum_thr=10000):
        for item_name, png in self.png_dict.items():
            if sum_thr == 10:
                cv2.imshow('corp', crop_im)
                # cv2.imshow('png', png)
                cv2.waitKey()
            sum = detect_item_sum(crop_im, png)
            if sum < sum_thr:
                return item_name

    def water_mark_classify(self, crop_im, sum_thr=10000, c_thr=10):
        most_color = find_most_color(crop_im)

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

    # screen = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/name/98k/98k.png')
    # fire_mode_detect = Detector('name', 'name')
    # a = fire_mode_detect.diff_sum_classify(screen)
    # print(a)

    import cv2
    import numpy as np
    from PIL import ImageGrab
    from pykeyboard import PyKeyboardEvent

    weapon_detect = Detector('name', 'name')
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
