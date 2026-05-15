# Gaussian blur is used to
# - Remove Noise
# - Smoothing or preprocessing

import cv2

# reading image
img = cv2.imread('../../img/earth.jpeg')
if img is None:
    print('Could not open image.')

# Gaussian Blur
blurred_image = cv2.GaussianBlur(img,(3,3),11) # kernel size should always be odd

cv2.imshow('gaussian_blur',blurred_image)
cv2.imshow('original_image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()