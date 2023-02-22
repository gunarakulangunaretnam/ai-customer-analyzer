import os
import cv2
import imutils
import numpy as np

ROI = 300
offset = 8
face_detection_offset = 20
width_and_hieght = 1000


prototxtPath = r"models\deploy.prototxt"
weightsPath = r"models\res10-300x300-ssd-iter-140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

cap = cv2.VideoCapture(1) #Camera 


def get_Center(x, y, w, h): # This function returns the center point of detected objects.
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


if not cap.isOpened():
    print("ERROR: Failed to open webcam")
    raise IOError("ERROR: Failed to open webcam")

while True:
    ret, frame = cap.read()
    resized_frame = imutils.resize(frame, width = width_and_hieght)

    (h, w) = resized_frame.shape[:2]
    blob = cv2.dnn.blobFromImage(resized_frame, 1.0, (224, 224),(104.0, 177.0, 123.0))

    faceNet.setInput(blob)
    detections = faceNet.forward()

    for i in range(0, detections.shape[2]):
        
        confidence = detections[0, 0, i, 2]
        
        if confidence > 0.5:
			# compute the (x, y)-coordinates of the bounding box for
			# the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            try:
                color = (0, 0, 255)
				# include the probability in the label
				#label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

				# display the label and bounding box rectangle on the output
				# frame

                cv2.putText(resized_frame, "face", (startX, startY - 10),
					cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (0, 255, 0), 2)


            except Exception as e:
                print(e)

    
    cv2.imshow('Display', resized_frame)

    waitKeyVal = cv2.waitKey(1)
    if waitKeyVal == 27:
        break

cap.release()
cv2.destroyAllWindows()