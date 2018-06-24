import cv2

cam = cv2.VideoCapture(0)
ret, image = cam.read()

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("webcam", image)

cv2.waitKey(0)
