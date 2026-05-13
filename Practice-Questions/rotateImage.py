import cv2

# reading image
img = cv2.imread('../img/watch.png')

# checking image
if img is None:
    print('Could not load image')
else:
    (h,w) =img.shape[:2]

    # find the center
    center = (w//2,h//2)

    # formula
    M = cv2.getRotationMatrix2D(center,-90,1.0)
    rotated = cv2.warpAffine(img,M,(w,h))

    cv2.imshow('Original_Image',img) # showing original image
    cv2.imshow('RotatedImage',rotated) # showing rotated image
    cv2.waitKey(0)
    cv2.destroyAllWindows()