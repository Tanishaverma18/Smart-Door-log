import cv2
import pickle
import numpy as np
import os
import csv
import time
from datetime import datetime
from win32com.client import Dispatch
from sklearn.neighbors import KNeighborsClassifier

class FaceRecognition:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        self.imgBackground = cv2.imread("background.png")
        self.COL_NAMES = ['NAME', 'TIME']
        self.load_data()
        self.train_knn()

    def load_data(self):
        """Load names and face data from pickled files."""
        with open('data/names.pkl', 'rb') as w:
            self.LABELS = pickle.load(w)
        with open('data/faces_data.pkl', 'rb') as f:
            self.FACES = pickle.load(f)

    def train_knn(self):
        """Train KNN classifier with the loaded face data."""
        self.knn = KNeighborsClassifier(n_neighbors=5)
        self.knn.fit(self.FACES, self.LABELS)

    def speak(self, text):
        """Use text-to-speech to announce attendance."""
        speaker = Dispatch("SAPI.SpVoice")
        speaker.Speak(text)

    def detect_faces(self):
        """Detect faces and update attendance."""
        while True:
            ret, frame = self.video.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.facedetect.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                crop_img = frame[y:y+h, x:x+w, :]
                resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
                output = self.knn.predict(resized_img)

                timestamp = datetime.now().strftime("%H:%M-%S")
                date = datetime.now().strftime("%d-%m-%Y")
                attendance = [str(output[0]), timestamp]

                self.draw_face_box(frame, x, y, w, h, str(output[0]))

                if cv2.waitKey(1) & 0xFF == ord('o'):
                    self.speak("Attendance Taken..")
                    self.save_attendance(date, attendance)

            self.imgBackground[162:162 + 480, 55:55 + 640] = frame
            cv2.imshow("Face Recognition", self.imgBackground)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.video.release()
        cv2.destroyAllWindows()

    def draw_face_box(self, frame, x, y, w, h, name):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (0,0,0), -1)
        cv2.putText(frame, name, (x, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

    def save_attendance(self, date, attendance):
        """Save attendance to a CSV file."""
        filename = f"Attendance/Attendance_{date}.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(self.COL_NAMES) 
            writer.writerow(attendance)

if __name__ == "__main__":
    fr = FaceRecognition()
    fr.detect_faces()