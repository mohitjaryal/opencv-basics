# Sharpening

import cv2
import numpy as np

img = cv2.imread('../../img/watch.png')

if img is None:
    print('Could not open image')

# created a kernel
sharpen_kernel = np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
# sharpening
sharped_img = cv2.filter2D(img,-1,sharpen_kernel)

cv2.imshow('sharped_image',sharped_img)
cv2.imshow('original_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()