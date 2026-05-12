# drawing shapes
import cv2
import numpy as np
import matplotlib.pyplot as plt

# creating an image
img = np.zeros((512,512,3))

# rectangle
# syntax -> .(imageName, point, point2, color, thickness of the rectangle)
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(255,0,0),thickness=3) # thickness=-1 -> filled rectangle

# circle
cv2.circle(img,center=(100,400),radius=50,color=(0,0,255),thickness=2) # thickness = -1 -> filled circle

# line
cv2.line(img,pt1=(0,0),pt2=(512,512),thickness=2,color=(0,255,0))

# adding text
cv2.putText(img,org=(100,100),fontScale=3,color=(255,255,0),thickness=1,lineType=cv2.LINE_AA,text='Hello',fontFace=cv2.FONT_HERSHEY_SIMPLEX)

cv2.imshow('window',img)
cv2.waitKey(0)