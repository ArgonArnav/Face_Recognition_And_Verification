import face_recognition
import cv2
import os
import urllib.request
import numpy as np
from utils import create_csv

# The output video
fourcc = cv2.VideoWriter_fourcc(*'WMV1')

url = 'http://[2401:4900:2e9d:8b50:9665:2dff:fe8d:7a30]:8080/shot.jpg'

output_movie = cv2.VideoWriter('video_output2.avi', fourcc, 20, (640, 480))

# Open the input movie file
input_movie = cv2.VideoCapture(url)
length = int(input_movie.get(cv2.CAP_PROP_FPS))

# Load some sample pictures and learn how to recognize them.
lmm_image = face_recognition.load_image_file("arnav.jpg")
lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]

al_image = face_recognition.load_image_file("arnav1.jpg")
al_face_encoding = face_recognition.face_encodings(al_image)[0]

a_image = face_recognition.load_image_file("toshitt.jpg")
a_face_encoding = face_recognition.face_encodings(a_image)[0]

a1_image = face_recognition.load_image_file("srmSIR.jpg")
a1_face_encoding = face_recognition.face_encodings(a1_image)[0]

known_faces = [
    lmm_face_encoding,
    al_face_encoding,
    a_face_encoding,
    a1_face_encoding
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

current_path = os.getcwd()

counter = 0
counter1 = 0

while True:
    # Grab a single frame of video
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    #if not ret:
    #    break

    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "arnav"
        elif match[1]:
            name = "arnav1"
        elif match[2]:
            name = "toshitt"
        elif match[3]:
            name="srmSIR"

        face_names.append(name)

    # Label the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        crop_img = frame[top:bottom, left:right]
        if (name == "arnav"):
            cv2.imwrite(current_path + "/face_database/arnav/" + "arnav" + str(counter) + ".png", crop_img)
            counter = counter + 1
        elif (name == "arnav1"):
            cv2.imwrite(current_path + "/face_database/arnav1/" + "arnav1" + str(counter1) + ".png", crop_img)
            counter1 = counter1 + 1
        elif (name == "toshitt"):
           cv2.imwrite(current_path + "/face_database/toshitt/" + "toshitt" + str(counter1) + ".png", crop_img)
           counter1 = counter1 + 1
        elif (name == "srmSIR"):
           cv2.imwrite(current_path + "/face_database/srmSIR/" + "srmSIR" + str(counter1) + ".png", crop_img)
           counter1 = counter1 + 1
     
          
        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    while True:
        imgResp = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8) 
        frame = cv2.imdecode(imgNp, -1)
        cv2.imshow('face_recog_crop', frame)
        cv2.waitKey(10)

    # Write the resulting image to the output video file
    output_movie.write(frame)
    print("Writing frame {} / {}".format(frame_number, length))

    
# All done!
input_movie.release()
output_movie.release()
cv2.destroyAllWindows()

create_csv.CreateCsv(current_path + "/face_database/")
