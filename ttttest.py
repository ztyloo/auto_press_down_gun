import cv2

im1 = cv2.imread('auto_hold_breath/test/17.png')

im2 = cv2.imread('auto_hold_breath/test/94.png')


diff = abs(im1-im2)

cv2.imshow('diff', diff)
cv2.waitKey(0)

