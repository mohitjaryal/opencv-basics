import cv2

img = cv2.imread('../img/watch.png')

cropped = img[50:100,100:150]

cv2.imshow('original',img)
cv2.imshow('cropped',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
