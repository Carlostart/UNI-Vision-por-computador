import numpy as np
import cv2
import matplotlib.pyplot as plt

path = 'Images/'

img = cv2.imread(path+'lily.tif')
# cv2.imshow('image',img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_image',gray_image)
cv2.imwrite(path+'lily_gray.tif', gray_image)

plt.hist(gray_image.ravel(),256,[0,256])
plt.show()

img = cv2.imread(path+'lily_gray.tif',1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.subplot(2,2,1)
plt.imshow(img)
plt.title('original')
plt.xticks([])
plt.yticks([])

retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
plt.subplot(2,2,2)
plt.imshow(threshold)
plt.title('threshold')
plt.xticks([])
plt.yticks([])

height = img.shape[0]
width = img.shape[1]

hr = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
plt.subplot(2,2,3)
plt.imshow(hr)
plt.title('halfresolution')
plt.xticks([])
plt.yticks([])

reduction = 50 # percentage
scale = int(reduction/2)
centerX,centerY=int(height/2),int(width/2)
radiusX,radiusY= int(scale*height/100),int(scale*width/100)

minX,maxX=centerX-radiusX,centerX+radiusX
minY,maxY=centerY-radiusY,centerY+radiusY

cropped = img[minX:maxX, minY:maxY]
resized_cropped = cv2.resize(cropped, (width, height))
plt.subplot(2,2,4)
plt.imshow(resized_cropped)
plt.title('zoomed')
plt.xticks([])
plt.yticks([])

plt.show()
# cv2.waitKey(0)
# cv2.closeAllWindows()
