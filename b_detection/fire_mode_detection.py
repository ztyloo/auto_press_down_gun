import os
import time
import cv2
import numpy as np



class Bb:
    def __init__(self):
        from_dir = 'b_detection/sub_im'
        # from_dir = 'sub_im'
        self.target_single = cv2.imread(os.path.join(from_dir, 'single.png'), cv2.IMREAD_UNCHANGED)
        self.target_burst = cv2.imread(os.path.join(from_dir, 'burst.png'), cv2.IMREAD_UNCHANGED)
        self.target_full = cv2.imread(os.path.join(from_dir, 'full.png'), cv2.IMREAD_UNCHANGED)
        self.mode = 'single'

    def set_screen(self, screen: np.ndarray):
        self.screen = screen

    def test(self):
        test_im = self.screen[1318: 1339, 1595: 1677, :]
        s_area = self.im_area_sum(test_im, self.target_single)
        b_area = self.im_area_sum(test_im, self.target_burst)
        f_area = self.im_area_sum(test_im, self.target_full)
        # print(s_area, b_area, f_area)
        max_area = max(s_area, b_area, f_area)
        if s_area == max_area:
            self.mode = 'single'
        elif s_area == max_area:
            self.mode = 'burst'
        else:
            self.mode = 'full'
        print(self.mode)

    def im_area_sum(self, im_3c: np.ndarray, im_4c: np.ndarray):
        test_im = im_3c.copy()
        shield = im_4c[:, :, [3]] // 255

        test_im = test_im * shield

        # cv2.imshow('target_im', target_im)
        # cv2.waitKey(2000)
        # cv2.imshow('test_im', test_im)
        # cv2.waitKey(2000)
        # print(np.sum(test_im ))

        return np.sum(test_im)


if __name__ == '__main__':
    from PIL import ImageGrab


    def get_screen(dir=None):
        if dir is None:
            screen = ImageGrab.grab()
            screen = np.array(screen)
            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
        else:
            screen = cv2.imread(dir)
        return screen

    b = Bb()
    dir = '../ctrl_cap'
    for path in os.listdir(dir):
        a_path = os.path.join(dir, path)
        print(a_path)
        screen = get_screen(a_path)
        b.set_screen(screen)
        b.test()






