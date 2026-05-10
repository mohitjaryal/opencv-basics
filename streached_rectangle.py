# create rectangle while drag

import cv2
import numpy as np

drawing = False
current_x = -1
current_y = -1

# Read image
img = np.zeros((512,512,3))

# Mouse event function
def draw(event, x, y, flags, param):

    global current_x, current_y, drawing
    # for click
    if event ==1:
        drawing = True # means start drawing

        # initial position
        current_x = x # start
        current_y = y

    # for drag
    elif event == 0:
        if drawing == True:
            cv2.rectangle(img,pt1=(current_x,current_y),pt2=(x,y),color=(0,255,255),thickness=-1)
    # for drop (leave mouse)
    elif event == 4:
        drawing = False
        cv2.rectangle(img,pt1=(current_x,current_y),pt2=(x,y),color=(255,0,0),thickness=-1)

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