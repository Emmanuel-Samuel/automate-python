# PROGRAMMER: EMMANUEL MAYOWA SAMUEL
# DATE CREATED: 15/03/2023
# REVISED DATE: 15/05/2023
# PURPOSE: Find faces in a video


# import modules
import cv2

# takes in path directory from user
input_video = str(input("Enter the name of the video including the path and extension: "))
# takes in output directory from user
output_video = str(input("Enter the output path of the video: "))

# reads the video file using video capture
file = cv2.VideoCapture(f'{input_video}')
# checks the video for frame and get the frames in numpy array
condition, frame = file.read()
# gets the number of frames as num_frames
num_frames = file.get(cv2.CAP_PROP_FRAME_COUNT)
# gets the number of frames per second as fps
fps = file.get(cv2.CAP_PROP_FPS)
# gets the video dimension as height
height = frame.shape[0]
# gets video dimension as width
width = frame.shape[1]

# prints the video information out
print(f"Video dimension is: {height} * {width} "
      f"Frames: {num_frames} FPS: {fps}")

# defines the path to the xml file
face_cascade = cv2.CascadeClassifier('/faces.xml')
# gets video to write on from input of user
output = cv2.VideoWriter(f'{output_video}/output.avi',
cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

# sets a timer to monitor process
timer = 0
# a loop to iterate over all the video frames
while success:
    faces = face_cascade.detectMultiScale(frame, 1.3, 4)
    # creates a rectangle over the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (150, 200, 255), 4)
    # writes new frames to output
    output.write(frame)
    # continues as long as condition is true
    condition, frame = file.read()
    timer += 1
    print(timer)

# releases the final video as output
output.release()
