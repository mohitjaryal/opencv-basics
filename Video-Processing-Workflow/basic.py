import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret -> will return True or False

    if not ret:
        print('Could not load ')
        break

    cv2.imshow('WebCam',frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        print('Tata, Goodbye')
        break

cap.release()
cv2.destroyAllWindows()