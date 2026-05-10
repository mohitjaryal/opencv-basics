# save image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading image
img = cv2.imread('./img/nature.jpg')

# the left top part of an image is it's origin

# cropping image
# we can do simple numpy slicing to crop an image
# syntax -> imageName[ height axis, width axis]
img_crop = img[100:300,200:500]

# saving image
cv2.imwrite('nature_small.png',img_crop)

cv2.imshow('window',img_crop)
cv2.waitKey(0)