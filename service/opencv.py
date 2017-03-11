import cv2
import numpy as np
import urllib2
 
cap = cv2.VideoCapture('http://127.0.0.1:8080/?action=stream')
while True:
     ret, frame = cap.read()
     cv2.imshow('Video', frame)
     if cv2.waitKey(1) == 27:
         exit(0)
