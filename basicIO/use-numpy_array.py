import cv2 as cv
import numpy as np

#using numpy array opreration

img = cv.imread('gavin.PNG')
#img[0,0] = [255,255,255]

#read # write image pix value
BlueValue=img.item(50,60,0)
print BlueValue
img.itemset((50,60,0),255)
print img.item(50,60,0)
img.itemset((50,60,0),BlueValue)
print img.item(50,60,0)

#print image three attributes
print img.shape
print img.size
print img.dtype

#set image all BGR-Green value is zero
#img = [;, ;, 1]=0

#set be interested area and replace to another area
my_area = img[0:50, 0:50]
img[100:150, 100:150] = my_area
cv.imwrite('gavin_area.png',img)

