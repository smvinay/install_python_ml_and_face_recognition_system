import face_recognition
import cv2
import os

known_encodings = []
known_names = []

dataset_path = "dataset"

# Load dataset
for file in os.listdir(dataset_path):

    image_path = os.path.join(dataset_path, file)

    image = face_recognition.load_image_file(image_path)
    encoding = face_recognition.face_encodings(image)[0]

    known_encodings.append(encoding)

    name = os.path.splitext(file)[0]
    known_names.append(name)

print("Dataset loaded")

video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    rgb = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

        matches = face_recognition.compare_faces(known_encodings, face_encoding)

        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_names[index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()
