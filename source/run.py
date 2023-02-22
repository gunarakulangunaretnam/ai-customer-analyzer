import os
import cv2
import time
import imutils
import threading
import numpy as np

ROI = 300
offset = 8
face_detection_offset = 20
width_and_hieght = 1000

processing_status = False

number_of_customer = 0


prototxtPath = r"models\deploy.prototxt"
weightsPath = r"models\res10-300x300-ssd-iter-140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

cap = cv2.VideoCapture(1) #Camera 


def get_center(x, y, w, h): # This function returns the center point of detected objects.
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


def main_processor():
    global processing_status, number_of_customer

    time.sleep(2)

    number_of_customer = number_of_customer + 1
    
    processing_status = False




if not cap.isOpened():
    print("ERROR: Failed to open webcam")
    raise IOError("ERROR: Failed to open webcam")

while True:
    ret, frame = cap.read()
    resized_frame = imutils.resize(frame, width = width_and_hieght)

    copy_frame = resized_frame.copy()

    cv2.line(resized_frame, (0 , ROI), (1200 , ROI), (0,255,255), 4)  # Line

    cv2.putText(resized_frame, f'Count:{number_of_customer} ', (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

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

                cv2.putText(resized_frame, "Customer", (startX, startY - 40),
					cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (0, 255, 0), 2)


                x = startX - face_detection_offset
                y = startY - face_detection_offset
                w = (endX + face_detection_offset) - startX
                h = (endY + face_detection_offset) - startY

                mid_point = get_center(int(x), int(y), int(w),int(h))
                cv2.circle(resized_frame, (mid_point[0], mid_point[1]), 6, color, -1)

                if mid_point[1] < (ROI + offset) and mid_point[1] > (ROI - offset):
                    cv2.line(resized_frame, (0 , ROI), (1200 , ROI), (0, 0, 255), 4)

                    if processing_status == False:
                        
                        face_roi = copy_frame[y:y+h+50, x:x+w+50]
                        cv2.imwrite("doc.jpg", face_roi)
                        
                        processing_status = True
                        main_function = threading.Thread(target=main_processor, args=(), daemon=True)
                        main_function.start()
                    
            except Exception as e:
                print(e)

    
    cv2.imshow('Display', resized_frame)

    waitKeyVal = cv2.waitKey(1)
    if waitKeyVal == 27:
        break

cap.release()
cv2.destroyAllWindows()