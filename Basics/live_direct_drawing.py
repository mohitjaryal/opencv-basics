import cv2
import numpy as np

# Read image
img = cv2.imread('../img/nature.jpg')

# Mouse event function
def draw(event, x, y, flags, param):

    if event ==1:
        cv2.circle(img,(x,y),radius=50,color=(255,0,0),thickness=-1)

# Create window once
cv2.namedWindow('window')

# Attach callback once
cv2.setMouseCallback('window', draw)

# Infinite loop
while True:

    # Show image
    cv2.imshow('window', img)

    # Press x to exit
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()