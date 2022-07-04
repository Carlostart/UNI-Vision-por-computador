import numpy as np
import cv2
import matplotlib.pyplot as plt

import histmatch as hm

path = '../Images/'
img = cv2.imread(path+'rice.tif')

# Input image
plt.subplot(2,4,1)
plt.imshow(img)
plt.title('Input image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,4,5)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.hist(gray_scale.ravel(),256,[0,255])
plt.title('Input image')
plt.ylim(top=1250)

# LUT enhancement
plt.subplot(2,4,2)
max = 200
min = 50
LUT=np.zeros(256,dtype=np.uint8)
LUT[max:]=255
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True)
lutimg=cv2.LUT(img, LUT)
plt.imshow(lutimg)
plt.title('LUT enhancement')
plt.xticks([])
plt.yticks([])

plt.subplot(2,4,6)
gray_scale = cv2.cvtColor(lutimg,cv2.COLOR_BGR2GRAY)
plt.hist(gray_scale.ravel(),256,[0,255])
plt.title('Histo LUT enhancement')
plt.ylim(top=1250)

# Equalized image
plt.subplot(2,4,3)
gray_scale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
equalized = cv2.equalizeHist(gray_scale)
plt.imshow(equalized,'gray')
plt.title('Equialized image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,4,7)
plt.hist(equalized.ravel(),256,[0,255])
plt.title('Equialized image')
plt.ylim(top=1250)


spec = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_ref = cv2.imread(path + 'tire.tif', cv2.IMREAD_GRAYSCALE)
spec = hm.hist_match(spec,img_ref)

plt.subplot(2,4,4)
plt.imshow(spec, 'gray')
plt.title('Specification enhancement')
plt.xticks([])
plt.yticks([])

plt.subplot(2,4,8)
plt.hist(spec.ravel(),256,[0,255])
plt.title('Histo specification enhancement')
plt.ylim(top=1250)

plt.show()