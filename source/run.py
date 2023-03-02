import os
import cv2
import time
import imutils
import threading
import numpy as np
from imutils.video import VideoStream
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


ROI = 300
offset = 8
face_detection_offset = 20
width_and_hieght = 1000

processing_status = False

number_of_customer = 0


prototxtPath = r"data\models\deploy.prototxt"
weightsPath = r"data\models\res10-300x300-ssd-iter-140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)


# load the face mask detector model from disk
maskNet = load_model("data\models\mask-detector.model")

cap = cv2.VideoCapture(0) #Camera 


def get_center(x, y, w, h): # This function returns the center point of detected objects.
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


def detect_and_predict_mask(frame, faceNet, maskNet):
	# grab the dimensions of the frame and then construct a blob
	# from it
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
		(104.0, 177.0, 123.0))

	# pass the blob through the network and obtain the face detections
	faceNet.setInput(blob)
	detections = faceNet.forward()

	# initialize our list of faces, their corresponding locations,
	# and the list of predictions from our face mask network
	faces = []
	locs = []
	preds = []

	# loop over the detections
	for i in range(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the detection
		confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the confidence is
		# greater than the minimum confidence
		if confidence > 0.5:
			# compute the (x, y)-coordinates of the bounding box for
			# the object
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			# ensure the bounding boxes fall within the dimensions of
			# the frame
			(startX, startY) = (max(0, startX), max(0, startY))
			(endX, endY) = (min(w - 1, endX), min(h - 1, endY))

			# extract the face ROI, convert it from BGR to RGB channel
			# ordering, resize it to 224x224, and preprocess it
			face = frame[startY:endY, startX:endX]
			face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
			face = cv2.resize(face, (224, 224))
			face = img_to_array(face)
			face = preprocess_input(face)

			# add the face and bounding boxes to their respective
			# lists
			faces.append(face)
			locs.append((startX, startY, endX, endY))

	# only make a predictions if at least one face was detected
	if len(faces) > 0:
		# for faster inference we'll make batch predictions on *all*
		# faces at the same time rather than one-by-one predictions
		# in the above `for` loop
		faces = np.array(faces, dtype="float32")
		preds = maskNet.predict(faces, batch_size=32)

		for (box, pred) in zip(locs, preds):
            # unpack the bounding box and predictions
			(startX, startY, endX, endY) = box
			(mask, withoutMask) = pred
			label = "Mask" if mask > withoutMask else "No Mask"

			return label


def main_processor():
    global processing_status, number_of_customer

    

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

                detection_data = detect_and_predict_mask(frame, faceNet, maskNet)

                if detection_data == "No Mask":
                    cv2.putText(resized_frame, "Customer (No Mask)", (startX, startY - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (0, 0, 255), 2)
                elif detection_data == "Mask":
                    cv2.putText(resized_frame, "Customer (Mask)", (startX, startY - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (255, 0, 0), 2)


                if mid_point[1] < (ROI + offset) and mid_point[1] > (ROI - offset):
                    cv2.line(resized_frame, (0 , ROI), (1200 , ROI), (0, 0, 255), 4)

                    if processing_status == False:

                        cv2.imwrite("data/cache-image.jpg", copy_frame)

                        
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