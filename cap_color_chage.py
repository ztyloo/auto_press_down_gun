import os
import cv2

for im_name in os.listdir('cap'):
    print(im_name)
    im = cv2.imread(os.path.join('cap', im_name))
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.join('cap', im_name), im)

