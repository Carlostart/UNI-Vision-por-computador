import cv2
import numpy as np

img = cv2.imread('images/lily_gray.tif')
cv2.imshow('original', img)

retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold', threshold)

height = img.shape[0]
width = img.shape[1]

hr = cv2.resize(img, (int(width/2), int(height/2)))
hr = cv2.resize(hr, (int(width), int(height)),interpolation = cv2.INTER_LINEAR_EXACT)
cv2.imshow('halfresolution', hr)

reduction = 50 # percentage
scale = int(reduction/2)
centerX,centerY=int(height/2),int(width/2)
radiusX,radiusY= int(scale*height/100),int(scale*width/100)

minX,maxX=centerX-radiusX,centerX+radiusX
minY,maxY=centerY-radiusY,centerY+radiusY

cropped = img[minX:maxX, minY:maxY]
resized_cropped = cv2.resize(cropped, (width, height))

cv2.imshow('zoomed', resized_cropped)

cv2.waitKey(0)
cv2.closeAllWindows()
