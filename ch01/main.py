import numpy as np
import cv2

img = cv2.imread("./assets/download.jpg",0)
img = cv2.resize(img,(400,400))
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)