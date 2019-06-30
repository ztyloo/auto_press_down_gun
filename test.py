import numpy as np
import cv2
from matplotlib import pyplot as plt


def get_rect_kernel(corner_len=30, thick=2):
    c_len = corner_len

    left_up_kernel = np.zeros((2*c_len+thick, 2*c_len+thick))
    right_up_kernel = np.zeros((2*c_len+thick, 2*c_len+thick))
    left_down_kernel = np.zeros((2*c_len+thick, 2*c_len+thick))
    right_down_kernel = np.zeros((2*c_len+thick, 2*c_len+thick))
    for i in range(c_len+thick):
        div = thick*(2*c_len+thick)

        for t in range(-thick//2, thick//2):
            left_up_kernel[2*c_len-i][c_len+t] = 1/div
            left_up_kernel[c_len+t][2*c_len-i] = 1/div

            right_up_kernel[2*c_len-i][c_len+t] = 1/div
            right_up_kernel[c_len+t][i] = 1/div

            right_down_kernel[i][c_len+t] = 1/div
            right_down_kernel[c_len+t][i] = 1/div

            left_down_kernel[i][c_len+t] = 1/div
            left_down_kernel[c_len+t][2*c_len-i] = 1/div

    return left_up_kernel, right_up_kernel, right_down_kernel, left_down_kernel


def find_corner_by_corner_canny(corner, canny):
    corner = cv2.filter2D(canny, -1, corner)
    gray_sort = np.sort(corner.flatten())[::-1]
    coordinate = np.where(corner > gray_sort[300])
    coordinate = coordinate[::-1]
    coordinate = list(map(list, zip(*coordinate)))
    return coordinate  # (x, y)


def get_possible_rectangle(lu_coord, ru_coord, rd_coord, ld_coord):
    blur_thr = 2
    possible_rectangle = list()
    for a, b in lu_coord:
        for aa, bb in ru_coord:
            if abs(bb-b) <= blur_thr and aa-a > 30:
                for aaa, bbb in rd_coord:
                    if abs(aaa-aa) <= blur_thr and bbb-bb > 30:
                        for aaaa, bbbb in ld_coord:
                            if abs(aaaa-a) <= blur_thr and abs(bbbb-bbb) <= blur_thr:
                                possible_rectangle.append((a, b, aaa, bbb))
    return possible_rectangle


if __name__ == '__main__':
    img = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/weapon/akm/akm.png')
    # img = cv2.imread('D:/github_project/auto_press_down_gun/image_detect/screen_captures/weapon/98k/98k.png')
    # img = img[120:170, 0:2238]
    # cv2.imshow('img', img)
    # cv2.waitKey()



    canny = cv2.Canny(img, 30, 100)/255
    cv2.imshow("canny", canny)
    cv2.waitKey()

    lu_c, ru_c, rd_c, ld_c = get_rect_kernel()
    lu_coor = find_corner_by_corner_canny(lu_c, canny)
    ru_coor = find_corner_by_corner_canny(ru_c, canny)
    rd_coor = find_corner_by_corner_canny(rd_c, canny)
    ld_coor = find_corner_by_corner_canny(ld_c, canny)

    cp_img = img.copy()
    for x, y in lu_coor:
        cv2.circle(cp_img, (x,y), 1, (255, 0, 0), -1)
    for x, y in ru_coor:
        cv2.circle(cp_img, (x,y), 1, (0, 255, 0), -1)
    for x, y in rd_coor:
        cv2.circle(cp_img, (x, y), 1, (0, 0, 255), -1)
    for x, y in ld_coor:
        cv2.circle(cp_img, (x,y), 1, (0, 255, 255), -1)
    cv2.imshow('img', cp_img)
    cv2.waitKey()

    possible_rect = get_possible_rectangle(lu_coor, ru_coor, rd_coor, ld_coor)

    cp2_img = img.copy()
    for x, y, x1, y1 in possible_rect:
        cv2.circle(cp2_img, (x, y), 1, (255, 0, 0), -1)
    for x, y, x1, y1 in possible_rect:
        cv2.circle(cp2_img, (x1, y), 1, (0, 255, 0), -1)
    for x, y, x1, y1 in possible_rect:
        cv2.circle(cp2_img, (x1, y1), 1, (0, 0, 255), -1)
    for x, y, x1, y1 in possible_rect:
        cv2.circle(cp2_img, (x, y1), 1, (0, 255, 255), -1)
    cv2.imshow('cp2_img', cp2_img)
    cv2.waitKey()







