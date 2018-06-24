import cv2

image = cv2.imread("pigeon.jpg")

y = 100
x = 50

roi = image[y: y + 50, x: x + 50]

cv2.imshow("Image", image)
cv2.imshow("ROI", roi)

roi[:, :] = (0, 255, 0)

cv2.imshow("Modified", image)

cv2.waitKey(0)
