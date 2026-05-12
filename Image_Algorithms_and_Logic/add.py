import numpy as np
import cv2
from matplotlib.pyplot import imshow

img1 = cv2.imread('../img/3D-Matplotlib.png')
img2 = cv2.imread('../img/mainsvmimage.png')

# addition operation
add = img1 + img2


# built in addition function in opencv
# add = cv2.add(img1,img2) # -> this adds all the pixel values

cv2.imshow('image', add)
cv2.waitKey(0)
cv2.destroyAllWindows()