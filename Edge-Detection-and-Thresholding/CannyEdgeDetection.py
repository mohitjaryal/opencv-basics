# Canny edge detection

import cv2
import numpy as np

img = cv2.imread('../img/earth.jpeg',cv2.IMREAD_GRAYSCALE)

edge = cv2.Canny(img,50,150) #threshold1 -> lower boundary, threshold2 -> upper boundry

cv2.imshow('image',img) # original image
cv2.imshow('edge',edge) # converted image
cv2.waitKey(0)
cv2.destroyAllWindows()

