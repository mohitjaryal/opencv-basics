import cv2
import  numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread("../img/nature.jpg")

# image
imgBlue = img[:,:,0]
imgGreen = img[:,:,1]
imgRed = img[:,:,2]

# creating a new image -> creating image side by side (horizontal stack)
new_img = np.hstack((imgBlue,imgGreen,imgRed))

# working with rgb
img[:,:,0] = 0 # color channels -> B = 0, G =1, R = 2

cv2.imshow("Original", new_img)
cv2.waitKey(0)