# flipping image
# we have 3 options to flip an image

import cv2
import numpy as np
import matplotlib.pyplot as plt

# reading image
img = cv2.imread('./img/nature.jpg')

# flipping image
# there are 3 flip code
# 0 = Vertical flip (around X-axis)
# 1 = Horizontal flip (around Y-axis)
# -1 = Both (horizontal + vertical)
img_flip = cv2.flip(img,-1)

cv2.imshow('window',img_flip)
cv2.waitKey(0)