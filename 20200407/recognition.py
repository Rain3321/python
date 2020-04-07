import face_recognition
import cv2
# https://github.com/ageitgey/face_recognition/blob/master/examples/facerec_from_video_file.py
# This is a demo of running face recognition on a video file and saving the results to a new video file.

# Open the input movie file
input_movie = cv2.VideoCapture("untitled.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')


# Load some sample pictures and learn how to recognize them.
pio_image = face_recognition.load_image_file("pio.jpg")
pio_face_encoding = face_recognition.face_encodings(pio_image)[0]
an_image = face_recognition.load_image_file("an.jpg")
an_face_encoding = face_recognition.face_encodings(an_image)[0]

known_faces = [
	pio_face_encoding,
	an_face_encoding,
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

numbering = [0 for _ in range(len(known_faces))]
while True:
    # Grab a single frame of video
	ret, frame = input_movie.read()
	frame_number += 1

    # Quit when the input video file ends
	if not ret:
		break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
	rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
	face_locations = face_recognition.face_locations(rgb_frame)
	face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
	face_names = []
	for face_encoding in face_encodings:
      # See if the face is a match for the known face(s)
		matchs = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.45)
		checking_point = 0
		
		for match in matchs:
			if match: 
				numbering[checking_point] += 1
			checking_point += 1


	print("Writing frame {} / {}".format(frame_number, length))

print(numbering)
print(matchs)
# All done!
input_movie.release()

cv2.destroyAllWindows()
