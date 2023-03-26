# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 15/03/2023
# REVISED DATE: 15/05/2023
# PURPOSE: Find faces in a webcam video live


# import modules
import cv2

# captures video from webcam and read the file
file = cv2.VideoCapture(0)
condition, frame = file.read()

# gets the height and width of the video
height = frame.shape[0]
width = frame.shape[1]

# gets the faces.xml file
face_cascade = cv2.CascadeClassifier('/faces.xml')
# releases the output to path defined
output = cv2.VideoWriter('/output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

# sets timer = 0
timer = 0
# loop to iterate the whole video frame
while condition:
    # creates a rectangle over the fame
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (150, 200, 255), 4)
    cv2.imshow("Recording", frame)
    # waits for 1 millisecond
    lock = cv2.waitKey(1)
    # press e on keyboard to end program
    if lock == ord('e'):
        break
    # writes frame to output video
    output.write(frame)
    # checks if condition is true
    condition, frame = file.read()
    # timer for number of frames
    timer += 1

# releases video output and ends windows opened
output.release()
file.release()
cv2.destroyALLWindows()