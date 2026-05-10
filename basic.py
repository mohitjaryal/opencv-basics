import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("./img/nature.jpg")

if img is None:
    print("Error: Image not found. Check the file path.")
else:
    print(img)

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print(type(img))

    # Display original
    cv2.imshow("Original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display grayscale
    cv2.imshow("Grayscale", img_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()