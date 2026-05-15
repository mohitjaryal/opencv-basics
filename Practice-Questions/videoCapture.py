# WAp to record video (taking input by user)

import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # frame width
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # frame height

# taking user input
user_input = int(input(
    'Hello welcome to Video Recording Program\n'
    'Do you wanna record video\n'
    '1. Yes (Enter 1)\n'
    '2. No (Enter 2)\n: '
))

codec = cv2.VideoWriter_fourcc(*'XVID')


# record video function
def record_video():

    record = cv2.VideoWriter(
        'video.avi',
        codec,
        20,
        (frame_width, frame_height)
    )

    while True:
        success, img = cap.read()

        if not success:
            break

        record.write(img)

        cv2.imshow('video', img)

        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cap.release()
    record.release()
    cv2.destroyAllWindows()


if user_input == 1:
    record_video()

else:
    print("Recording cancelled")