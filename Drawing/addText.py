# WAP to add text in image

import cv2

img = cv2.imread('../img/earth.jpeg')

if img is None:
    print('Could not open image')
else:
    cv2.putText(img,
                text='Hello everyone, I am EARTH',
                org=(50,250),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.2,
                color=(255,255,255),
                thickness=5)
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
