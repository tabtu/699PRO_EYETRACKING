#!/usr/bin/env python
'''
Capture Faces Version 1.1 Written by Tab Jul.1 2017
'''
from __future__ import print_function

import numpy as np
import cv2
from PIL import Image

# local modules
from video import create_capture
from common import clock, draw_str

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)

    cascade_fn = args.get('--cascade', "../data/haarcascades/haarcascade_frontalface_alt.xml")
    cascade = cv2.CascadeClassifier(cascade_fn)
    cam = create_capture(video_src, fallback='synth:bg=../data/error.jpg:noise=0.05')

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        rects = detect(gray, cascade)

        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        print(rects)

        for x1, y1, x2, y2 in rects:
            roi = gray[y1:y2, x1:x2]
            cv2.imwrite('faces.jpg', roi)
            cv2.imshow('face', roi)

        cv2.imwrite("videocap.jpg", vis)


        cv2.imshow('facedetect', vis)

        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
