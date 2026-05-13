# WAP to draw circle on an image

import cv2

img = cv2.imread('../img/watch.png')

if img is None:
    print('Could not open image')
else:
    cv2.circle(img,center=(250,250),radius=100,color=(255,255,255),thickness=-1)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()