# WAP to read,show,save and convert image (taking input from user)

import cv2

# user input
file_inp = input('Enter file path: ')

# load image
img = cv2.imread(file_inp)

# check image
if img is None:
    print("Image not found. Check the file path.")
    exit()

opp_inp = int(input('Enter what you wanna do?\n1. Show image\n2. Save Image\n3. Both\n: '))

# convert to grayscale
def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# show image
def show(image):
    cv2.imshow('window', image)
    cv2.waitKey(0)

# save image
def save(image):
    cv2.imwrite('gray_output.png', image)

# processing grayscale
gray_img = convert_gray(img)

# user choice logic
if opp_inp == 1:
    show(gray_img)

elif opp_inp == 2:
    save(gray_img)

elif opp_inp == 3:
    save(gray_img)
    show(gray_img)

else:
    print('Invalid choice')

cv2.destroyAllWindows()