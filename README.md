# Smart Door Log System (A Binary Search Application)🔒🚪✨ 
An AI-powered system that automatically marks attendance using face recognition. This project uses OpenCV, K-Nearest Neighbors (KNN), and Tkinter to detect and recognize faces from a webcam feed, log attendance with timestamps, and provide a user-friendly interface for searching and managing attendance records.

## Features🌟💻
* Real-Time Face Detection: Uses OpenCV to detect faces via webcam.
* Face Recognition: Identifies users using the K-Nearest Neighbors (KNN) algorithm.
* Voice Feedback: Once attendance is marked, the system provides voice confirmation with "Attendance marked!".
* Popup Confirmation: A simple pop-up appears confirming that the attendance has been successfully recorded.
* Attendance Logs: All attendance records are saved in a CSV file with timestamps.
* Searchable Attendance Logs: View and search through previous attendance logs, including timestamps, with a clean Tkinter GUI.

## How It Works👇
* OpenCV captures your face from the webcam feed.
* The KNN algorithm matches your face to the stored data.
* Once recognized, the system provides voice feedback: "Attendance marked!"
* The attendance is logged with timestamp in a CSV file.
* The Tkinter GUI allows users to view and search through previous attendance logs by date and time.

## Technologies Used⚙️
* Python: The main programming language used for the project.
* OpenCV: For face detection and capturing webcam feed in real-time.
* K-Nearest Neighbors (KNN): A machine learning algorithm used to recognize faces.
* Tkinter: A GUI library for building the user interface to view and manage attendance.
* pyttsx3: A text-to-speech library for voice feedback after marking attendance.
* Pickle: For saving and loading face data.
* CSV: For storing attendance records with timestamps.
