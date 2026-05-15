# Median blur

import cv2

img = cv2.imread('../../img/earth.jpeg')

if img is None:
    print('Could not open the image')

# median blur
median_blur = cv2.medianBlur(img,17)

cv2.imshow('median_blur',median_blur)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()