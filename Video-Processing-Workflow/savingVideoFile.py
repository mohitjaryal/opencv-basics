# Saving video file using OpenCV

import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'XVID')

# Add file extension like .avi
record = cv2.VideoWriter(
    'video.avi',
    codec,
    20,
    (frame_width, frame_height)
)

while True:
    success, img = cap.read()   # FIXED

    if not success:
        break

    record.write(img)
    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# Release camera also
cap.release()
record.release()
cv2.destroyAllWindows()