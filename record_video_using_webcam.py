import  cv2
import  numpy as np

capture = cv2.VideoCapture(0)
fourcc  = cv2.VideoWriter_fourcc(*'XVID')
# writer object
out = cv2.VideoWriter('sampe.avi',fourcc, 20.0,(640,480))

while True:
    ret, frame = capture.read() # reading continuously
    out.write(frame) # write
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow('webcam',img_gray)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

out.release()
capture.release()
cv2.destroyAllWindows()