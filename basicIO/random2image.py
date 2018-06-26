import cv2
import numpy
import os

#Make an array of 300*400 = 120,000 random bytes.
randomByterArray = bytearray(os.urandom(120000))
flatNumpyArray = numpy.array(randomByterArray)

#Convert the array to makr a 400*300 grayscale image.
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)

#Convert the array to make a 400*100 color image
bgrImge = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImge)
