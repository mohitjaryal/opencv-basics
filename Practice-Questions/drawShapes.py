# WAP to draw different shapes taking input by user

import cv2

# user input
file_inp = input('Enter file path: ')

# load image
img = cv2.imread(file_inp)

if img is None:
    print('Could not open image')
    exit()

opp = int(input('What do you want to perform\n1. Draw Line\n2. Draw Rectangle\n3.Draw Circle\n:'))


def line(img,pt1,pt2):
    cv2.line(img,pt1,pt2,color=(255,255,255),thickness=6)

def circle(img,center,radius):
    cv2.circle(img,center,radius,color=(255,255,255),thickness=-1)

def rectangle(img,pt1,pt2):
    cv2.rectangle(img,pt1,pt2,color=(255,255,255),thickness=3)

# line
if opp == 1:
    pt1 = tuple(map(int, input("Enter point 1 :").split(',')))
    pt2 = tuple(map(int, input("Enter point 2 :").split(',')))
    line(img,pt1,pt2)
# rectangle
elif opp ==2:
    pt1 = tuple(map(int, input("Enter point 1 :").split(',')))
    pt2 = tuple(map(int, input("Enter point 2 :").split(',')))
    rectangle(img, pt1, pt2)
# center
elif opp ==3:
    center = tuple(map(int, input("Enter center of the circle :").split(',')))
    radius = int(input('Enter radius:'))
    circle(img,center,radius)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()