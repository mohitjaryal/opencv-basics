# draw rectangle
import cv2

 # reading image
img = cv2.imread('../img/watch.png')

if img is None:
     print('Could not find image')
else:
    # to draw the rectangle -> use .rectangle()
    cv2.rectangle(img,pt1=(50,50),pt2=(250,250),color=(255,255,255),thickness=6)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()