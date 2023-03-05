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

To install the above packages, use the following command.
pip install numpy opencv-python

To install the face_recognition, install the dlib package first.
pip install dlib

Now, install face_recognition module using the below command
pip install face_recognition

Steps to develop face recognition model
Before moving on, let’s know what face recognition and detection are.

Face recognition is the process of identifying or verifying a person’s face from photos and video frames.

Face detection is defined as the process of locating and extracting faces (location and size) in an image for use by a face detection algorithm.

Face recognition method is used to locate features in the image that are uniquely specified. The facial picture has already been removed, cropped, scaled, and converted to grayscale in most cases. Face recognition involves 3 steps: face detection, feature extraction, face recognition.

OpenCV is an open-source library written in C++. It contains the implementation of various algorithms and deep neural networks used for computer vision tasks.

Summary
In this machine learning project, we developed a face recognition model in python and opencv using our own custom dataset.
