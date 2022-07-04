import numpy as np
import cv2
import matplotlib.pyplot as plt

path = '../Images/'

img = cv2.imread(path+'lily.tif')
# cv2.imshow('image',img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray_image',gray_image)
cv2.imwrite('images/lily_gray.tif', gray_image)

img=plt.hist(gray_image.ravel(),256,[0,256])
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
