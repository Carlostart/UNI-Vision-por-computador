import cv2
import matplotlib.pyplot as plt
import numpy as np

path = '../Images/'
img = cv2.imread('C:/Users/Carlo/OneDrive/Escritorio/Images/coin.jpg',0)

plt.subplot(2,2,1)
plt.imshow(img, 'gray')
plt.title('Imagen original')
plt.xticks([])
plt.yticks([])

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
# retval, sobelx = cv2.threshold(sobelx, 100, 255, cv2.THRESH_BINARY)
abs_sobel64f = np.absolute(sobelx)
sobelx = np.uint8(abs_sobel64f)

abs_sobel64f = np.absolute(sobely)
sobely = np.uint8(abs_sobel64f)

mask = sobelx + sobely

retval, mask = cv2.threshold(mask,130,255,cv2.THRESH_BINARY)
# retval, sobelx = cv2.threshold(sobelx, 100, 255, cv2.THRESH_BINARY)
# retval, sobely = cv2.threshold(sobely, 100, 255, cv2.THRESH_BINARY)

mask=cv2.bitwise_not(mask)
fg = cv2.bitwise_or(img, img, mask=mask)

mask = cv2.bitwise_not(mask)
fg = cv2.cvtColor(fg, cv2.COLOR_GRAY2BGR)
cols, rows, retval = fg.shape
background = np.zeros((cols, rows, 3), np.uint8)

background[:] = (0, 255, 0)
bk = cv2.bitwise_or(background, background, mask=mask)

final = cv2.bitwise_or(fg, bk)

plt.subplot(2,2,2)
plt.imshow(sobelx, 'gray')
plt.title('Imagen Sobel horizontal')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(sobely, 'gray')
plt.title('Imagen Sobel vertical')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(final)
plt.title('Imagen de bordes (verde) sobre la original')
plt.xticks([])
plt.yticks([])

plt.show()
