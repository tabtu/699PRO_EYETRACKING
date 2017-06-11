import numpy as np
import cv2

def detectFaces(image_name):
    img = cv2.imread(image_name)
    face_cascade = cv2.CascadeClassifier("data/haarcascades/haarcascade_frontalface_alt.xml")
    if img.ndim == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img #if语句：如果img维度为3，说明不是灰度图，先转化为灰度图gray，如果不为3，也就是2，原图就是灰度图

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.3和5是特征的最小、最大检测窗口，它改变检测结果也会改变
    result = []
    for (x, y, width, height) in faces:
        result.append((x, y, x+width, y+height))
    return result



cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 直方图均衡处理
        gray = cv2.equalizeHist(gray)
        # 脸部特征分类地址，里面还有其他
        cascade_fn = 'data/haarcascades/haarcascade_frontalface_alt.xml'
        # 读取分类器,CascadeClassifier下面有一个detectMultiScale方法来得到矩形
        cascade = cv2.CascadeClassifier(cascade_fn)

        cv2.imshow('EyesTracking', frame)
        k = cv2.waitKey(60) & 0xff
        if k == 27:
            break
        else:
            #print("continue")
            #cv2.imwrite(chr(k)+".jpg", img2)
    else:
        print("error")
        break
cv2.destroyAllWindows()
cap.release()
