import cv2
import numpy as np

cv2.namedWindow('test')
face_cascade=cv2.CascadeClassifier('/Users/Kevin/Documents/Workspace/PycharmProjects/test/haarcascade_frontalface_default.xml')

img=cv2.imread(filename)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray,1.3,5)
for (x,y,h,w) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.namedWindow('faces Detected!')
cv2.imshow('faces Detected!',img)
cv2.imwrite('faces.jpg',img)
cv2.waitKey(0)
