import cv2

cap = cv2.VideoCapture('1.mp4')

ret, frame = cap.read()
i = 0
while ret:
    print(i)
    cv2.imwrite(str(i)+'.png', frame)
    i += 1
    ret, frame = cap.read()
