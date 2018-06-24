import cv2

cam = cv2.VideoCapture(0)

lower_green = (55, 130, 65)
upper_green = (75, 175, 70)

while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, lower_green, upper_green)
    cv2.imshow("threshold", mask)

    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
