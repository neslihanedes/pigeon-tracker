import cv2

cam = cv2.VideoCapture(0)

lower_green = (100, 85, 70)
upper_green = (120, 110, 85)

while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(frame, lower_green, upper_green)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                      cv2.CHAIN_APPROX_SIMPLE)

    # find biggest contour
    # biggest means max area
    if len(contours) > 0:
        yoshi = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(yoshi)

        print("x=" + str(x) + "; y=" + str(y))

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

    cv2.imshow("tracked yoshi", frame)

    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
