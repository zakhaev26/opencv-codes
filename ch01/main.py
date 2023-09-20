import numpy as np
import cv2

img = cv2.imread("./assets/soubhik.png",0)
# cv2.namedWindow("Image",cv2.WINDOW_NORMAL)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.imwrite("output.jpg",img)
with open("pixels.txt","w")as fp:
    fp.write(str(img))
    fp.close()

