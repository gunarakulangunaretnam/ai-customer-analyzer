import os
import cv2
import imutils

cap = cv2.VideoCapture(0)

width_and_hieght = 1000

if not cap.isOpened():
    print("ERROR: Failed to open webcam")
    raise IOError("ERROR: Failed to open webcam")

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width = width_and_hieght)
    cv2.imshow('Display', frame)

    waitKeyVal = cv2.waitKey(1)
    if waitKeyVal == 27:
        break

cap.release()
cv2.destroyAllWindows()