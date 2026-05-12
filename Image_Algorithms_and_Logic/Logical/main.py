import numpy as np
import cv2

img1 = cv2.imread('../img/3D-Matplotlib.png')
img2 = cv2.imread('../watch.png')

row,cols,channels = img2.shape
roi = img1[0:row,0:cols]


cv2.waitKey(0)
cv2.destroyAllWindows()