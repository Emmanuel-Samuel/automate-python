# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 15/03/2023
# REVISED DATE: 15/05/2023
# PURPOSE: Censoring Faces using other pictures


# import modules
import cv2

# Load the video
file = cv2.VideoCapture("C:/Users/emmas/Desktop/faces/mayor_2.mp4")

# Load the cat face image
meme = cv2.imread("C:/Users/emmas/Desktop/faces/meme.png",1)

# Get the first frame and the width and height of the video
condition, frame = file.read()
width = frame.shape[1]
height = frame.shape[0]

# Load the face cascade
face_cascade = cv2.CascadeClassifier('C:/Users/emmas/Desktop/faces.xml')

# Prepare the video object where the output video will be stored
output_video = cv2.VideoWriter('C:/Users/emmas/Desktop/faces/output.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))

# Read the frames one by one, detect faces, and overlay the meme face on them
count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)
    for (x, y, w, h) in faces:
        meme1 = cv2.resize(meme, (w, h))
        place = frame[y:y+h, x:x+w]
        cv2.imwrite('C:/Users/emmas/Desktop/faces/meme1.jpg', place)
        marsh = cv2.addWeighted(place, 0, meme1, 1, 0)
        cv2.imwrite("C:/Users/emmas/Desktop/faces/meme2.jpg", marsh)
        frame[y:y+h, x:x+w] = marsh
    output_video.write(frame)
    condition, frame = file.read()
    count += 1
    print(count)

output_video.release
