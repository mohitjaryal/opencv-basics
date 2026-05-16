# Bitwise not
# convert black to white, white to black

import cv2
import numpy as np

img1 = np.zeros((300,300), dtype=np.uint8)

cv2.circle(img1,(150,150),100,255,-1)

bitwise_opp = cv2.bitwise_not(img1)

cv2.imshow('circle',img1)
cv2.imshow('bitwise_or', bitwise_opp)

cv2.waitKey(0)
cv2.destroyAllWindows()