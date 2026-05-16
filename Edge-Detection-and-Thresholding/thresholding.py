import  cv2

img = cv2.imread('../img/earth.jpeg',cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Could not open the image!')

"""
90 - 0 black
130 - 255 white
180 - 255 white
50 - 0  black
"""
ret, thresholded_image = cv2.threshold(img,120,255,cv2.THRESH_BINARY)


cv2.imshow('original',img)
cv2.imshow('thresholded_image',thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()