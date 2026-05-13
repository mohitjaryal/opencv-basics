# WAP to flip image
import cv2

# reading image
img = cv2.imread('../img/nature.jpg')

# checking image
if img is None:
    print('Could not find image')
else:

    # flipCode -> tells how to flip the image
    # 0 -> vertically (top to bottom)
    # 1 -> horizontally (left ot right)
    # -1 -> both horizontally and vertically
    flip =cv2.flip(img,0)
    cv2.imshow('Original_Image',img) # original image
    cv2.imshow('Flipped_Image',flip) # flipped image
    cv2.waitKey(0)
    cv2.destroyAllWindows()