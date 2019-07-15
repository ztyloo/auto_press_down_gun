import cv2
import numpy as np
import matplotlib.pyplot as plt


def is_there_bullet_hole(im, rect=None):
    bullet_hole_max_energy = 30
    bullet_hole_min_confidence = 253

    if rect is not None:
        dx0, dy0, dx1, dy1 = rect
        im = im[dy0:dy1, dx0:dx1, :]

    im_grey = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im_black = np.where(im_grey < bullet_hole_max_energy, 255, 0).astype(np.uint8)

    hole_kernel = get_hole_kernel()
    hole_confidence = cv2.filter2D(im_black, -1, hole_kernel)
    max_hole_conf = np.max(hole_confidence)
    if max_hole_conf > bullet_hole_min_confidence:
        return True
    return False


def find_bullet_hole(im, rect=None):
    height_resolution = 10
    bullet_hole_max_energy = 15
    bullet_hole_min_confidence = 253

    dx0, dy0 = 0, 0
    if rect is not None:
        dx0, dy0, dx1, dy1 = rect
        im = im[dy0:dy1, dx0:dx1, :]

    im_grey = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    im_black = np.where(im_grey < bullet_hole_max_energy, 255, 0).astype(np.uint8)

    hole_kernel = get_hole_kernel()
    hole_confidence = cv2.filter2D(im_black, -1, hole_kernel)
    hole_position = np.where(hole_confidence > bullet_hole_min_confidence, 255, 0).astype(np.uint8)
    # cv2.imshow('hole_position', hole_position)

    _, labels, stats, centroids = cv2.connectedComponentsWithStats(hole_position)

    res_centers = list()
    last_y1, last_area = 0, 10000
    for stat, center in zip(stats[1:], centroids[1:]):
        x0, y0, width, height, area = stat
        if abs(last_y1-y0) < height_resolution:
            if area > last_area:
                res_centers.pop()
                res_centers.append([int(center[0]+dx0), int(center[1]+dy0)])
                last_y1 = y0+height
                last_area = area
        else:
            res_centers.append([int(center[0]+dx0), int(center[1]+dy0)])
            last_y1 = y0+height
            last_area = area

    return res_centers


def find_up_first(im, rect=None):
    res_centers = find_bullet_hole(im, rect)
    if len(res_centers) > 0:
        return res_centers[-1]
    return []


def find_down_first(im, rect=None):
    res_centers = find_bullet_hole(im, rect)
    if len(res_centers) > 0:
        return res_centers[0]
    return []


def get_hole_kernel(radius=8):
    hole_kernel = np.zeros((2*radius+1, 2*radius+1))

    area = 0
    for j in range(-2*radius, 2*radius+1):
        for i in range(-2*radius, 2*radius+1):
            if np.linalg.norm(np.array([i, j]) - np.array([radius, radius])) <= radius:
                hole_kernel[i, j] = 1
                area += 1
    hole_kernel /= area
    return hole_kernel


if __name__ == '__main__':
    from press_gun.generate_distance.find_aim_point import find_aim_point

    for i in range(20):
        screen = cv2.imread('D:/github_project/auto_press_down_gun/press_gun/generate_distance/aug/'+str(i)+'.png')

        aim_point = find_aim_point(screen)
        bullet_hole_centers = find_bullet_hole(screen, rect=(1500, 250, 1900, aim_point[1] - 20))

        for center in bullet_hole_centers:
            x, y = center
            im = cv2.circle(screen, (int(x), int(y)), 5, (255, 0, 255), thickness=20)

        cv2.imshow('screen', screen)
        cv2.waitKey()
