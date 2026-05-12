import cv2
import  numpy as np

img = cv2.imread('../img/nature.jpg')

crop_img = False
current_x = -1
current_y = -1

# event listener
def crop(event,x,y,flags,param):
    global  crop_img, current_x, current_y
    if event == 1:
        crop_img =  True
        current_x = x
        current_y = y
    elif event == 4:
        end_x = x
        end_y = y

        crop_img = False
        cv2.rectangle(img,pt1=(current_x, current_y),pt2=(x, y), thickness=1, color=(255, 0, 0))
        # crop tool
        cropped = img[current_y:end_y,current_x:end_x]
        cv2.imshow('new_window',cropped)
        cv2.waitKey(0)

cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',crop)

while True:
    cv2.imshow('window',img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()