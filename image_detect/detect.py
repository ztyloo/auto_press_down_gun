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

    def diff_sum_classify(self, crop_im, sum_thr=10000, absent_return='', check=False):
        for item_name, png in self.png_dict.items():
            sum = detect_3d_sum(crop_im, png)
            if sum < sum_thr:
                return item_name
        if check:
            cv2.imshow('crop_im', crop_im)
            cv2.waitKey()
        return absent_return

    def canny_classify(self, crop_im, sum_thr=10000):
        canny = cv2.Canny(crop_im, 200, 200)
        min_item = None
        min_sum = 1000000
        for item_name, png in self.png_dict.items():
            sum = detect_1d_sum(canny, cv2.Canny(png, 200, 200))
            if sum < min_sum:
                min_item = item_name
                min_sum = sum
        return min_item

    def water_mark_classify(self, crop_im, sum_thr=10000, c_thr=10):
        # most_color = find_most_color(crop_im)
        # diff_crop = crop_im - np.array(most_color)[np.newaxis, np.newaxis, :]
        # shield = (np.where(diff_crop.sum(axis=-1) <= 20 , 255, 0)//255)[:, :, np.newaxis].astype(np.uint8)
        # crop_im *= shield

        min_item = None
        min_sum = 1000000
        for item_name, png in self.png_dict.items():
            sum = detect_3d_sum(crop_im, png)
            if sum < min_sum:
                min_item = item_name
                min_sum = sum
        return min_item


def detect_1d_sum(detect_im, target_im, blur=1):
    min_test_res = 1000000000000
    for dx in range(-blur, blur+1):
        for dy in range(-blur, blur+1):
            test_im = detect_im.copy()
            M = np.float32([[1, 0, dx], [0, 1, dy]])
            test_im = cv2.warpAffine(test_im, M, (test_im.shape[1], test_im.shape[0]))

            sum = np.sum(test_im - target_im)
            min_test_res = min(sum, min_test_res)
    return min_test_res


def detect_3d_sum(detect_im_3c: np.ndarray, target_im_4c: np.ndarray, blur=0):
    target_im = target_im_4c[:, :, 0:3]
    shield = (target_im_4c[:, :, [3]] // 255).astype(np.uint8)
    target_im = target_im * shield

    # cv2.imshow('target_im', target_im)
    # cv2.waitKey()

    test_im = detect_im_3c.copy()
    for dy in range(-20, 20):
        M = np.float32([[1, 0, 0], [0, 1, 0]])
        target_im = cv2.warpAffine(target_im, M, (test_im.shape[1], test_im.shape[0]))

        cv2.imshow('test_im - target_im', test_im - target_im)
        cv2.waitKey()

    min_test_res = 1000000000000
    for dx in range(-blur, blur+1):
        for dy in range(-blur, blur+1):
            test_im = detect_im_3c.copy()
            M = np.float32([[1, 0, dx], [0, 1, dy]])
            test_im = cv2.warpAffine(test_im, M, (test_im.shape[1], test_im.shape[0]))

            test_im = test_im * shield
            sum = np.sum(test_im - target_im)
            min_test_res = min(sum, min_test_res)

    # print(min_test_res)
    return min_test_res


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
    from auto_position_label.crop_position import crop_screen, screen_position as sc_pos

    # fire_mode_detect = Detector('fire_mode')
    # for i in range(25):
    #     path = 'D:/github_project/auto_press_down_gun/image_detect/temp_test_image/'+str(i)+'.png'
    #     screen = cv2.imread(path)
    #     crop_im = crop_screen(screen, sc_pos['fire_mode'])
    #     a = fire_mode_detect.canny_classify(crop_im)
    #     print(a)
    #     cv2.imshow('crop_im', crop_im)
    #     cv2.waitKey()

    # fire_mode_detect = Detector('small_fire_mode')
    # a = fire_mode_detect.canny_classify(crop_screen(screen, sc_pos['small_fire_mode']))
    # print(a)

    path = 'D:/github_project/auto_press_down_gun/auto_position_label/screen_captures/scope/15/18.png'
    screen = cv2.imread(path)
    scope_detect = Detector('scope')
    a = scope_detect.diff_sum_classify(crop_screen(screen, sc_pos['weapon']['0']['scope']))
    print(a)

    # path = 'D:/github_project/auto_press_down_gun/temp_test_image/444.png'
    # crop_im = cv2.imread(path)
    # scope_detect = Detector('scope')
    # a = scope_detect.diff_sum_classify(crop_im)
    # print(a)
