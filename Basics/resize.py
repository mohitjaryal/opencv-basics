# resizing image

import cv2
import  numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread("../img/nature.jpg")

# resizing
img_resize = cv2.resize(img,(256,256))

# printing size
print(img_resize.size)

cv2.imshow('original', img_resize)
cv2.waitKey(0)