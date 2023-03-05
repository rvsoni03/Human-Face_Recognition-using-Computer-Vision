import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
 
video_capture = cv2.VideoCapture(0)
 
emp1_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\1.jpg")
emp1_encoding = face_recognition.face_encodings(emp1_image)[0]

emp2_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\2.jpg")
emp2_encoding = face_recognition.face_encodings(emp2_image)[0]
 
ratan_tata_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\ratanTata.png")
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]
 
emp3_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\3.jpg")
emp3_encoding = face_recognition.face_encodings(emp3_image)[0]
 
emp4_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\4.jpg")
emp4_encoding = face_recognition.face_encodings(emp4_image)[0]

emp5_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\5.jpg")
emp5_encoding = face_recognition.face_encodings(emp5_image)[0]

emp6_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\6.jpg")
emp6_encoding = face_recognition.face_encodings(emp6_image)[0]

emp7_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\dataset1\\img\\7.jpg")
emp7_encoding = face_recognition.face_encodings(emp7_image)[0]

emp8_image = face_recognition.load_image_file("C:\\Users\\hp5cd\\Downloads\\projects\\facialDetection\\1.jpg")
emp8_encoding = face_recognition.face_encodings(emp8_image)[0]

 
known_face_encoding = [
emp1_encoding,
emp2_encoding,
ratan_tata_encoding,
emp3_encoding,
emp4_encoding,
emp5_encoding,
emp6_encoding,
emp7_encoding,
emp8_encoding,

]
 
known_faces_names = [
"emp1",
"emp2",
"ratan tata",
"emp3",
"emp4",
"emp5",
"emp6",
"emp7",
"emp8"
]
 
students = known_faces_names.copy()
 
face_locations = []
face_encodings = []
face_names = []
s=True
 
 
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
 
 
 
f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)
 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name+' Present', 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
f.close()