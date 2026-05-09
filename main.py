# importing 
import cv2 # opencv
import numpy as np # importing numpy
import matplotlib.pyplot as plt


img = cv2.imread('watch.png',cv2.IMREAD_GRAYSCALE)

# showing image through open cv
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# showing image through matplotlib
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()