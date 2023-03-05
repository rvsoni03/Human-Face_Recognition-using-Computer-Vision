# Human-Face_Recognition-using-Computer-Vision
The project implements feature based face recognition system which first finds any face or faces in the color image and then matches it against the database to recognize the individuals.
In this python project, we are going to build a machine learning model that recognizes the persons from an image. We use the face_recognition API and OpenCV in our project.

Tools and Libraries
python 3.10.8
numpy
opencv
face-recognition
dlib
os

**To install the above packages, use the following command.**

pip install numpy opencv-python

**To install the face_recognition, install the dlib package first.**

pip install dlib

**Now, install face_recognition module using the below command**

pip install face_recognition

**Steps to develop face recognition model**
Before moving on, let’s know what face recognition and detection are.

Face recognition is the process of identifying or verifying a person’s face from photos and video frames.

Face detection is defined as the process of locating and extracting faces (location and size) in an image for use by a face detection algorithm.

Face recognition method is used to locate features in the image that are uniquely specified. The facial picture has already been removed, cropped, scaled, and converted to grayscale in most cases. Face recognition involves 3 steps: face detection, feature extraction, face recognition.

OpenCV is an open-source library written in C++. It contains the implementation of various algorithms and deep neural networks used for computer vision tasks.

How to run ?
Make sure have executable permission. (chmod 777 .)
pip install -r requirements.txt

Please make sure that you have folders called 'datasets' and 'trainer' in the same directory. (Optional, I have put the code so it will create if it's not exist.)

Run in the command line the face_datasets.py for taking your face image as datasets. Don't forget to set each person's face to unique ID (You need to edit the code everytime, or maybe just change the id variable to raw_input[OPTIONAL])

If you have more face to be include, change the ID and run the program again

Train your datasets by running attendance.py

lastly run the attendance.py file and a webcam is open then show the pitcure of employee then the webcam recognize the face and enter the name of the person whose face was recognized by webcam in the csv file.
The time and date on which the face recognized was done is also enters in csv file.



Summary
In this machine learning project, we developed a face recognition model in python and opencv using our own custom dataset.
