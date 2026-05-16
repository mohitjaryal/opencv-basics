# Bitwise or
#  it is used to combine two images

import cv2
import numpy as np

img1 = np.zeros((300,300), dtype=np.uint8)
img2 = np.zeros((300,300), dtype=np.uint8)

cv2.circle(img1,(150,150),100,255,-1)
cv2.rectangle(img2, (150,150), (250,250), 255, -1)

bitwise_opp = cv2.bitwise_or(img1, img2)

cv2.imshow('circle',img1)
cv2.imshow('rectangle',img2)
cv2.imshow('bitwise_or', bitwise_opp)

cv2.waitKey(0)
cv2.destroyAllWindows()