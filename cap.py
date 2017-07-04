import numpy as np
import cv2
from PIL import Image, ImageDraw

cv2.namedWindow('cap')
cap = cv2.VideoCapture(0)
success, frame = cap.read()
#color = (0, 0, 0)
face_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_alt.xml")

while(success):
    success, frame = cap.read()
    cv2.imshow('origin', frame)

    if frame.ndim == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = frame

    cv2.imshow('gray', gray)

    cv2.equalizeHist(gray, gray)

    ##divisor = 8
    ##h, w = size
    ##minSize = (w//divisor, h//divisor)
    #faceRects = face_cascade.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)

    #rects = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=0, minSize=10, maxSize=50)
    #recvs = face_cascade.detectMultiScale(gray[1.2, scaleFactor[5, minNeighbors[0, flags[10, minSize[50, maxSize]]]]])
    #recvs = face_cascade.detectMultiScale(gray, 1.2, 5, 0)

    cv2.imshow('cap', gray)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
    else:
        print("continue")

cv2.destroyAllWindows()
cap.release()
