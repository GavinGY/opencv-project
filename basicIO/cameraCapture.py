#coding=utf-8
import cv2 
import time

#cv2.namedWindow("camera",1)
#开启ip摄像头
ipCamera="http://admin:admin@192.168.42.129:8081/" 
capture =cv2.VideoCapture(ipCamera)

num = 0;
while True:
    success,img = capture.read()
    cv2.imshow("camera",img)

    #按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
    key = cv2.waitKey(10) 

    if key == 27:
    #esc键退出
        print("esc break...")
        break
    if key == ord(' '):
        #保存一张图像
        print("save image")
        num = num+1
        filename = "cameraCaptureFrames_%s.jpg" % num
        cv2.imwrite(filename,img)

capture.release()
#cv2.destroyWindow("camera")
cv2.destroyAllWindows()

