'''

 * Date:            23-02-2023
 * Organization:    Deep11
 * Author:          Gunarakulan Gunaretnam
 * Author Email:    gunarakulan@gmail.com
 * Author Likedin:  https://www.linkedin.com/in/gunarakulangunaretnam/
 * Author GitHub:   https://github.com/gunarakulangunaretnam 

  Source Info
  -----------
  This is the vision analyzer script of the AI Customer Analyzer project; it
  can analyze facial attributes of humans: Age, Gender, Race, Emotions, Mask and
  this script can count customers and update all the information to the database. 


 '''

import os
import cv2
import uuid
import json
import time
import pygame
import imutils
import datetime
import threading
import numpy as np
import mysql.connector
from ftplib import FTP
import tensorflow as tf
from deepface import DeepFace
from imutils.video import VideoStream
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

### START DATABASE CONNECTION ###
database_host = ""
database_user = ""
database_pass = ""
database_name = ""

with open('data\\database-credentials.json') as f:
    config_data = json.load(f)

    # Access the values from the dictionary
    database_host = config_data['database_host']
    database_user = config_data['database_user']
    database_pass = config_data['database_password']
    database_name = config_data['database_name']

mydb = mysql.connector.connect(
  host = database_host,
  user = database_user,
  password = database_pass,
  database = database_name
)

mycursor = mydb.cursor()

### END DATABASE CONNECTION ###

### START FTP CONNECTION ###

ftp_host = ""
ftp_username = ""
ftp_password = ""


with open("data\\ftp-credentials.json") as ftp_file:
    config_data = json.load(ftp_file)

    # Access the values from the dictionary
    ftp_host = config_data['ftp_host']
    ftp_username = config_data['ftp_username']
    ftp_password = config_data['ftp_password']

### END FTP CONNECTION ###



### START GET TOTOAL NUMBER OF COUNTING OF THE DAY ###

current_date = datetime.datetime.now().strftime('%d-%m-%Y')
query_to_get_total_numbers = "SELECT COUNT(*) FROM vision_data WHERE date = current_date"
mycursor.execute(query_to_get_total_numbers) # Execute the query
number_of_customer = mycursor.fetchone()[0] # Get the count

### END GET TOTOAL NUMBER OF COUNTING OF THE DAY ###


### START GET VOICE LANGUAGE FROM SETTINGS TABLE ###

query_to_get_lang = "SELECT _value FROM setting WHERE _key = 'voice_lang'"
mycursor.execute(query_to_get_lang) # Execute the query
fetch_data = mycursor.fetchall() # Fetch all data
greeting_language = fetch_data[0][0] 

### END GET VOICE LANGUAGE FROM SETTINGS TABLE ###

pygame.mixer.init()

ROI = 300
offset = 8
width_and_hieght = 1000
face_detection_offset = 20
processing_status = False
cap = cv2.VideoCapture(1) #Camera 


prototxtPath = r"data\models\deploy.prototxt"
weightsPath = r"data\models\res10-300x300-ssd-iter-140000.caffemodel"
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)


# load the face mask detector model from disk
maskNet = load_model("data\models\mask-detector.model")


def greeting_function():

    global greeting_language

    currentHour = int(datetime.datetime.now().hour)
    basicGreeting = ""

    if currentHour >= 0 and currentHour < 12:

        if greeting_language == "English":
            pygame.mixer.music.load('data\\greeting-voices\\english-good-morning.mp3')
            pygame.mixer.music.play()

        elif greeting_language == "Tamil":
            pygame.mixer.music.load('data\\greeting-voices\\tamil-good-morning.mp3')
            pygame.mixer.music.play()

        
        elif greeting_language == "Sinhala":
            pygame.mixer.music.load('data\\greeting-voices\\sinhala-good-morning.mp3')
            pygame.mixer.music.play()



    if currentHour >= 12 and currentHour < 18:

        if greeting_language == "English":

            pygame.mixer.music.load('data\\greeting-voices\\english-good-afternoon.mp3')
            pygame.mixer.music.play()

        elif greeting_language == "Tamil":
            pygame.mixer.music.load('data\\greeting-voices\\tamil-good-afternoon.mp3')
            pygame.mixer.music.play()
        
        elif greeting_language == "Sinhala":
            pygame.mixer.music.load('data\\greeting-voices\\sinhala-good-afternoon.mp3')
            pygame.mixer.music.play()

    if currentHour >= 18 and currentHour != 0:

        if greeting_language == "English":
            pygame.mixer.music.load('data\\greeting-voices\\english-good-evening.mp3')
            pygame.mixer.music.play()

        elif greeting_language == "Tamil":
            pygame.mixer.music.load('data\\greeting-voices\\tamil-good-evening.mp3')
            pygame.mixer.music.play()
        
        elif greeting_language == "Sinhala":
            pygame.mixer.music.load('data\\greeting-voices\\sinhala-good-evening.mp3')
            pygame.mixer.music.play()


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
		preds = maskNet.predict(faces, batch_size=32, verbose=0)

		for (box, pred) in zip(locs, preds):
            # unpack the bounding box and predictions
			(startX, startY, endX, endY) = box
			(mask, withoutMask) = pred
			label = "Mask" if mask > withoutMask else "No Mask"

			return label


def upload_image_to_server_ftp(image):
    try:  
        ftp = FTP(ftp_host)
        ftp.login(user=ftp_username, passwd=ftp_password)
        ftp.sendcmd("TYPE I")
        with open(f"predictions/{image}", "rb") as f:
            ftp.storbinary(f"STOR {image}", f)
            print("Step 03: Image Uploaded Remotely!")

    except Exception as e:
        print(f"FTP Image Upload Failed: {e}")


def database_updater(image_frame, image_url, mask, age, age_category, gender, emotion, race):

    data_date_and_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    _date = data_date_and_time.split(' ')[0].strip()
    _time =  data_date_and_time.split(' ')[1].strip()

    data = {
    'date': _date,
    'time': _time,
    'image_url': image_url,
    'mask': "Not Found" if mask == "No Mask" else "Found",
    'age': age,
    'age_category':age_category,
    'gender': gender.capitalize(),
    'emotion':emotion.capitalize(),
    'race': race.capitalize()
    }

    insert_query = ("INSERT INTO vision_data (date, time, image_url, mask, age, age_category, gender, emotion, race) "
         "VALUES (%(date)s, %(time)s, %(image_url)s, %(mask)s, %(age)s, %(age_category)s, %(gender)s, %(emotion)s, %(race)s)")

    mycursor.execute(insert_query, data)
    mydb.commit()

    # Here Call FTP function that uploads the image to the server

    print("Step 04: Database Updated!")


def image_saver(frame, coordinates, mask_data, predicted_age, predicted_gender, predicted_emotion, predicted_race):
    
    cv2.rectangle(frame, (coordinates['x'], coordinates['y']), (coordinates['x'] + coordinates['w'], coordinates['y'] + coordinates['h']), (255, 0, 0), 2)
    
    if mask_data == "No Mask":
        cv2.putText(frame, f"Mask: Not Found", (coordinates['x'],coordinates['y']-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    
    elif mask_data == "Mask":
        cv2.putText(frame, f"Mask: Found", (coordinates['x'],coordinates['y']-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    age_category = ""

    predicted_age = int(predicted_age) # Convert STR to INT

    if  predicted_age >= 0 and predicted_age <= 12:
        age_category = "Kid"

    elif predicted_age >= 13 and predicted_age <= 19:
        age_category = "Teenage"

    elif predicted_age >= 20 and predicted_age <= 64:
        age_category = "Adult"

    elif predicted_age >= 65 and predicted_age <= 100:
        age_category = "Elder"


    replaced_emotion = ""

    if predicted_emotion.lower() == "fear":
        replaced_emotion = "surprise"

    else:
        replaced_emotion = predicted_emotion


    rece_replaced = ""

    if predicted_race.lower() == "indian" or predicted_race.lower() == "latino hispanic" or predicted_race.lower() == "middle eastern":
        rece_replaced = "asian"

    else:
        rece_replaced = predicted_race


    
    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    cv2.putText(frame, f'{current_time} ', (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(frame, f"Age: {str(predicted_age).capitalize()} ({age_category})", (coordinates['x']+coordinates['w']+10,coordinates['y']+30), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.putText(frame, f"Gender: {str(predicted_gender).capitalize()}", (coordinates['x']+coordinates['w']+10,coordinates['y']+60), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.putText(frame, f"Emotion: {str(replaced_emotion).capitalize()}", (coordinates['x']+coordinates['w']+10,coordinates['y']+90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv2.putText(frame, f"Race: {str(rece_replaced).capitalize()}", (coordinates['x']+coordinates['w']+10,coordinates['y']+120), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    

    image_name = uuid.uuid4()
    
    cv2.imwrite(f"predictions/{image_name}.jpg",frame)

    print("Step 02: Image Saved Locally!")

    upload_image_to_server_ftp(f"{image_name}.jpg")
    database_updater(frame, f"{image_name}.jpg", mask_data, predicted_age, age_category, predicted_gender, replaced_emotion, rece_replaced)


def face_analyzer(frame, mask_detection_data, face_region):

    global processing_status, number_of_customer

    #Call greeting function in thread
    greeting_voice_function = threading.Thread(target=greeting_function, args=(), daemon=True)
    greeting_voice_function.start()

    predicted_age = ""
    predicted_gender = ""
    predicted_emotion = ""
    predicted_race = ""

    try:      

        # When there is not mask, send for face analyzing.
        if mask_detection_data == "No Mask":
            face_attributes = DeepFace.analyze(frame, actions = ['age', 'gender', 'race', 'emotion'])
            print("Step 01: Face Analyzed!")
            image_saver(frame, face_attributes[0]['region'], mask_detection_data, face_attributes[0]["age"], face_attributes[0]["dominant_gender"], face_attributes[0]["dominant_emotion"], face_attributes[0]["dominant_race"])

        # When there is mask, do not send for face analyzing, only update the database.      
        elif mask_detection_data == "Mask":

            print("Step 01: Face Analyzing Failed: (Face with Mask)")

            predicted_age = "NONE"
            predicted_gender = "NONE"
            predicted_emotion = "NONE"
            predicted_race = "NONE"

            image_saver(frame, face_region, mask_detection_data, predicted_age, predicted_gender, predicted_emotion, predicted_race)


        number_of_customer = number_of_customer + 1

    except Exception as e:
        print(f'Error: {e}')

        # When there is no mask but, face not found, do not send for face analyzing, only update the database.    
        if str(e).strip() == "Face could not be detected. Please confirm that the picture is a face photo or consider to set enforce_detection param to False.":

            print("Step 01: Face Analyzing Failed: (Face not Found)")

            predicted_age = "NONE"
            predicted_gender = "NONE"
            predicted_emotion = "NONE"
            predicted_race = "NONE"

            image_saver(frame, face_region, mask_detection_data, predicted_age, predicted_gender, predicted_emotion, predicted_race)

    time.sleep(2)
    processing_status = False


if not cap.isOpened():
    print("ERROR: Failed to open webcam")
    raise IOError("ERROR: Failed to open webcam")

while True:
    ret, frame = cap.read()
    resized_frame = imutils.resize(frame, width = width_and_hieght)

    copy_frame = resized_frame.copy()

    cv2.line(resized_frame, (0 , ROI), (1200 , ROI), (0,255,255), 4)  # Line

    current_time = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    cv2.putText(resized_frame, f'{current_time} ', (5, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.putText(resized_frame, f'Count:{number_of_customer} ', (5, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

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

                mask_detection_data = detect_and_predict_mask(frame, faceNet, maskNet)

                if mask_detection_data == "No Mask":
                    cv2.putText(resized_frame, "Customer (No Mask)", (startX, startY - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
                    cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (0, 0, 255), 2)
                elif mask_detection_data == "Mask":
                    cv2.putText(resized_frame, "Customer (Mask)", (startX, startY - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    cv2.rectangle(resized_frame, (startX-face_detection_offset, startY-face_detection_offset), (endX+face_detection_offset, endY+face_detection_offset), (255, 0, 0), 2)


                face_region = {'x': x, 'y': y, 'w': w, 'h': h}

                if mid_point[1] < (ROI + offset) and mid_point[1] > (ROI - offset):
                    cv2.line(resized_frame, (0 , ROI), (1200 , ROI), (0, 0, 255), 4)

                    if processing_status == False:
                        processing_status = True

                        #Call main_processer
                        face_analyzer_function = threading.Thread(target=face_analyzer, args=(copy_frame,mask_detection_data, face_region), daemon=True)
                        face_analyzer_function.start()

            except Exception as e:
                print(e)

    
    cv2.imshow('Display', resized_frame)

    waitKeyVal = cv2.waitKey(1)
    if waitKeyVal == 27:
        break

cap.release()
cv2.destroyAllWindows()