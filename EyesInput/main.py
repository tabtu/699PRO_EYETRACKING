'''
Capture Faces Version 1.3 Written by Tab Aug.18 2017
'''

from __future__ import print_function

import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str
from eyescmp import classify_gray_hist, classify_hist_with_split,classify_aHash,classify_pHash

def detect(img, cascade):
    # setup classify recognizer
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# draw rects on screen
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print(__doc__)

    # setup video capture.
    # can also use cv2.VideoCapture(0)
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)

    # setup cascade modules.
    # haarcascades files include frontalface and eyes.
    cascade_fn = args.get('--cascade', "../data/haarcascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "../data/haarcascades/haarcascade_eye.xml")
    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    # install web camera.
    cam = create_capture(video_src, fallback='synth:bg=../data/error.jpg:noise=0.05')
    while True:
        # read image stream from video capture.
        ret, img = cam.read()
        # change image to gray.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # equalizing gray image.
        gray = cv2.equalizeHist(gray)
        # setup clock if needed.
        #t = clock()
        # detect faces from equalized gray image.
        rects = detect(gray, cascade)
        # copy a color image for showing.
        vis = img.copy()
        # draw squals on screen where have found faces.
        draw_rects(vis, rects, (0, 255, 0))
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
                for x3, y3, x4, y4 in subrects:
                    eyea = gray[y3:y4, x3:x4]
                    cv2.imwrite('1.jpg', eyea)
                    try: eyeb
                    except:
                        eyeb = gray[y3:y4, x3:x4]
                        x3b = x3
                        y3b = y3
                        x4b = x4
                        y4b = y4
                    else:
                        #if x3-x3b+x4-x4b+y3-y3b+y4-y4b < 200:
                        cv2.imwrite('2.jpg', eyeb)
                        img1 = cv2.imread('1.jpg')
                        img2 = cv2.imread('2.jpg')
                        degree = classify_pHash(img1, img2)
                        print (degree)
                    #cv2.imshow('eyes', eyea)
        cv2.imshow('face', vis)
        cv2
        if cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
