import cv2
import numpy as np


def search_for_aim_point(im, rect=(1420, 420, 2020, 1020)):
    aim_point_max_energy = 5
    aim_point_min_confidence = 60

    dx0, dy0, dx1, dy1 = 0, 0, 0, 0
    if rect is not None:
        dx0, dy0, dx1, dy1 = rect
        im = im[dy0:dy1, dx0:dx1, :]

    im_grey = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im_black = np.where(im_grey < aim_point_max_energy, 255, 0).astype(np.uint8)
    aim_point_kernel = get_6_aim_point_kernel()
    aim_point_confidence = cv2.filter2D(im_black, -1, aim_point_kernel)
    hole_position = np.where(aim_point_confidence > aim_point_min_confidence, 255, 0).astype(np.uint8)

    _, labels, stats, centroids = cv2.connectedComponentsWithStats(hole_position)
    return int(centroids[-1][0] + dx0), int(centroids[-1][1] + dy0)


def get_6_aim_point_kernel(radius=300):
    thickness = 4
    aim_point_kernel = np.zeros((2*radius+thickness, 2*radius+thickness))

    area = 0
    for j in range(-2*radius, 2*radius+1):
        for i in range(-2*radius, 2*radius+1):
            if radius < i <= radius+thickness or radius < j <= radius+thickness:
                aim_point_kernel[i, j] = 1
                area += 1
    aim_point_kernel /= area
    return aim_point_kernel


if __name__ == '__main__':
    for i in range(20):
        screen = cv2.imread('D:/github_project/auto_press_down_gun/press_gun/generate_distance/aug/'+str(i)+'.png')

        x0, y0 = search_for_aim_point(screen)
        im = cv2.circle(screen, (int(x0), int(y0)), 5, (255, 0, 255), thickness=20)

        cv2.imshow('screen', screen)
        cv2.waitKey()
