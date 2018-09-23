import cv2

shield = cv2.imread('shield.png')
shield = shield / 255.0

screen = cv2.imread('cap/44.png')
origin = screen[46:81, 1620:1818, :]

screen2 = cv2.imread('cap/380.png')
origin2 = screen2[46:81, 1620:1818, :]

diff = abs(origin-origin2) * shield
# diff = origin - origin2

cv2.imshow('diff', diff)
cv2.waitKey(0)

