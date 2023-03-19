# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 15/03/2023
# REVISED DATE: 15/05/2023
# PURPOSE: Censoring Faces using Blurred Area


# import modules
import cv2

# loads the video, reads and get video info(width, height)
file = cv2.VideoCapture('C:/Users/emmas/Desktop/faces/mayor_2.mp4')
condition, frame = file.read()
height = frame.shape[0]
width = frame.shape[1]

# Load face cascade file
face_cascade = cv2.CascadeClassifier('C:/Users/emmas/Desktop/faces.xml')

# Defines path for output video
output_video = cv2.VideoWriter('C:/Users/emmas/Desktop/faces/output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# timer for program runtime
timer = 0
# loop for iterating frames, creates rectangle over faces
while condition:
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)
    for (x, y, w, h) in faces:
        frame[y:y+h, x:x+w] = cv2.blur(frame[y:y+h, x:x+w], (50, 50))

    output_video.write(frame)
    condition, frame = file.read()
    timer += 1
    print(timer)

output_video.release()
