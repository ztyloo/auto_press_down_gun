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
        test_im = self.screen[1130: 1152, 1519: 1920, :]

        if self.im_area_sum(test_im, self.target_single) < 100000:
            print('single')
            self.mode = 'single'
            return True
        elif self.im_area_sum(test_im, self.target_burst) < 100000:
            print('burst')
            self.mode = 'burst'
            return True
        elif self.im_area_sum(test_im, self.target_full) < 100000:
            print('full')
            self.mode = 'full'
            return True
        else:
            print('fire mode detection failed!!!')
            return False

    def im_area_sum(self, im_3c: np.ndarray, im_4c: np.ndarray):
        test_im = im_3c.copy()
        target_im = im_4c[:, :, 0:3]
        shield = im_4c[:, :, [3]] // 255

        test_im = test_im * shield
        target_im = target_im * shield

        cv2.imshow('target_im', target_im)
        cv2.waitKey(2000)
        cv2.imshow('test_im', test_im)
        cv2.waitKey(2000)
        print(np.sum(test_im - target_im))

        return np.sum(test_im - target_im)


if __name__ == '__main__':
    from PIL import ImageGrab


    def get_screen():
        screen = ImageGrab.grab()
        screen = np.array(screen)
        screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

        # screen = cv2.imread('screens/burst.png')
        # screen = cv2.imread('screens/single.png')
        # screen = cv2.imread('screens/full.png')
        return screen

    time.sleep(5)
    b = Bb()
    b.screen = get_screen()
    b.test()
    b.screen = get_screen()
    b.test()
    b.screen = get_screen()
    b.test()




