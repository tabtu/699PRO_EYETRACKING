import numpy as np
import cv2
from PIL import Image, ImageDraw

cv2.namedWindow('test')
cap = cv2.VideoCapture(0)
success, frame = cap.read()
color = (0, 0, 0)
face_cascade = cv2.CascadeClassifier('/data/haarcascades/haarcascade_frontalface_alt.xml')

while(success):
    success, frame = cap.read()
    #ret = True
    #frame = cv2.imread("test1.jpg", 0)
    size = frame.shape[:2]

    if frame.ndim == 3:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    #cv2.equalizeHist(gray, gray)

    divisor = 8
    h, w = size
    minSize = (w//divisor, h//divisor)
    #faceRects = face_cascade.detectMultiScale(gray, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)

    #rects = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, flags=0, minSize=10, maxSize=50)
    #recvs = face_cascade.detectMultiScale(gray[1.2, scaleFactor[5, minNeighbors[0, flags[10, minSize[50, maxSize]]]]])
    resul = face_cascade.detectMultiScale(gray[1.2, scaleFactor[5, minNeighbors[0, flags[10, minSize[100, maxSize]]]]])

    #cv2.imshow('EyesTracking', gray)
    cv2.imshow('test', gray)
    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break
    else:
        print("continue")
cv2.destoryWindow('test')
cap.release()
