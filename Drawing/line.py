# draw line
import cv2

img = cv2.imread('../img/nature.jpg')

if img is None:
    print('Could not open the image.')
else:
    cv2.line(
        img,
        pt1=(50,100),
        pt2=(300,300),
        color=(255,255,255),
        thickness=5
    )

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()