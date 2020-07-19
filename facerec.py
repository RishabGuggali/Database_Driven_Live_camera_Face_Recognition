import face_recognition
import cv2
import psycopg2

video_capture = cv2.VideoCapture(0)



#connect to the db
con = psycopg2.connect(
            #host = " ",
            database="Sample",
            user = "postgres",
            password = "rishab")

#cursor
cur = con.cursor()

cur.execute("select Name,Image from Users")
rows = cur.fetchall()


known_face_names=[]
known_face_encodings =[]
for r in rows:
    known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(r[1]))[0])

    known_face_names.append(r[0])

#----------------------------------------------------------------------------------------------------------------------

while True:
    ret, frame = video_capture.read()

    rgb_frame = frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Random Person"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255),2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        if (name != "Random Person"):
            print(name, "was here")
    cv2.imshow('Video', frame)

    # Q to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break