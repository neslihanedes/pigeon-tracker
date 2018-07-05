import cv2

video = cv2.VideoCapture('/home/kiview/Videos/GOPR0523.mp4')
lower_red = (170, 100, 100)
upper_red = (180, 255, 255)

skip_to_frame = 1100
frame_number = 0

while video.isOpened():
    frame_number += 1
    print(frame_number)

    if frame_number < skip_to_frame:
        video.grab()
        continue

    ret, image = video.read()

    if ret:
        hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        color_tracking_mask = cv2.inRange(hsv_frame, lower_red, upper_red)

        _, contours, _ = cv2.findContours(color_tracking_mask, cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_SIMPLE)

        # find biggest contour
        # biggest means max area
        if len(contours) > 0:
            tracked_object = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(tracked_object)
            print("x=" + str(x) + "; y=" + str(y))
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), thickness=3)

        cv2.imshow('tracking_mask', color_tracking_mask)
        cv2.imshow('hsv', hsv_frame)
        cv2.imshow('original', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("video closed")
video.release()
cv2.destroyAllWindows()
