import cv2
import numpy as np


class Aim_Point:
    def __init__(self):
        kernal_root = 'D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_image/'
        self.kernal_dict = dict()
        for k in [4, 6, 8, 15]:
            k_path = kernal_root + str(k) + '.png'
            k_im = cv2.imread(k_path)
            self.kernal_dict[str(k)] = k_im

        self.aim_point_max_energy = 5
        self.aim_point_min_confidence = 60

    def search_aim_point(self, im, scope):
        aim_point_kernel = self.kernal_dict[str(scope)]
        kernal_sum = np.sum(aim_point_kernel)
        im_grey = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
        im_black = np.where(im_grey < self.aim_point_max_energy, 255, 0).astype(np.uint8)
        aim_point_confidence = cv2.filter2D(im_black, -1, aim_point_kernel/kernal_sum)
        hole_position = np.where(aim_point_confidence > self.aim_point_min_confidence, 255, 0).astype(np.uint8)
        _, labels, stats, centroids = cv2.connectedComponentsWithStats(hole_position)
        return int(centroids[-1][0]), int(centroids[-1][1])

    def get_6_aim_point_kernel(self, radius=300):
        thickness = 4
        aim_point_kernel = np.zeros((2 * radius + thickness, 2 * radius + thickness))

        area = 0
        for j in range(-2 * radius, 2 * radius + 1):
            for i in range(-2 * radius, 2 * radius + 1):
                if radius < i <= radius + thickness or radius < j <= radius + thickness:
                    aim_point_kernel[i, j] = 1
                    area += 1
        aim_point_kernel /= area
        return aim_point_kernel


if __name__ == '__main__':
    i = 4
    radius = 100
    screen = cv2.imread('D:/github_project/auto_press_down_gun/auto_hold_breath/kernal_screen/'+str(i)+'.png')
    screen = screen[720-radius:720+radius, 1720-radius:1720+radius]

    aim_point = Aim_Point()
    x0, y0 = aim_point.search_aim_point(screen, str(i))
    im = cv2.circle(screen, (int(x0), int(y0)), 2, (255, 0, 255), thickness=2)

    cv2.imshow('screen', screen)
    cv2.waitKey()
