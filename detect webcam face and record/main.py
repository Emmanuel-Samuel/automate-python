# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 15/03/2023
# REVISED DATE: 15/05/2023
# PURPOSE: Find faces in a webcam video


# import modules
import cv2

file = cv2.VideoCapture(0)
condition, frame = file.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('C:/Users/emmas/Desktop/faces.xml')
output = cv2.VideoWriter('C:/Users/emmas/Desktop/faces/output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

timer = 0
while condition:
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (150, 200, 255), 4)
    output.write(frame)
    condition, frame = video.read()
    timer += 1

output.release()
