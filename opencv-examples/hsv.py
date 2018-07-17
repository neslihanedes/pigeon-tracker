import cv2

cam = cv2.VideoCapture(0)

x, y, w, h = 200, 200, 100, 100

while cam.isOpened():
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # ROI is actually fake, we just look at one pixel
    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), thickness=1)

    print(frame[y + 1, x + 1])

    cv2.putText(frame, "HSV: {0}".format(frame[y + 1, x + 1]), (x, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=2)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) & 0xff
    if key == 27:
        break
