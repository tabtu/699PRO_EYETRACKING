#!/usr/bin/env python
# encoding: utf-8

import cv2
import numpy as np


img = cv2.imread('eyes.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  # gray
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY) #binary
cv2.imshow("enumerate", binary)

#contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) # edge
#cv2.drawContours(img,contours,-1,(0,0,255),3)

#cv2.imshow("img", img)
cv2.waitKey(0)
