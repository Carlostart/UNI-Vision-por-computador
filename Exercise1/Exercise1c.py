import cv2
import matplotlib.pyplot as plt
import numpy as np

path = 'Images/'
img = cv2.imread(path+'blood.tif',0)

# Gaussian noise
row,col= img.shape
ch = 0
mean = 0
var = 300
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col))
gauss = gauss.reshape(row,col)
noisy = (img + gauss).astype(np.uint8)

plt.subplot(2,2,1)
plt.imshow(noisy, 'gray')
plt.title('Gaussian noise')
plt.xticks([])
plt.yticks([])

avg = cv2.blur(noisy,(3,3))

plt.subplot(2,2,2)
plt.imshow(avg, 'gray')
plt.title('Averaging smoothing')
plt.xticks([])
plt.yticks([])

median = cv2.medianBlur(noisy, 3)
plt.subplot(2,2,3)
plt.imshow(median, 'gray')
plt.title('Median smoothing')
plt.xticks([])
plt.yticks([])

gaussian = cv2.GaussianBlur(noisy,(3,3),0.5)
plt.subplot(2,2,4)
plt.imshow(gaussian, 'gray')
plt.title('Gaussian smoothing')
plt.xticks([])
plt.yticks([])

plt.show()

s_vs_p = 0.5
amount = 0.1
out = np.copy(img)
# Salt mode
num_salt = amount * img.size * s_vs_p

coords = [list(np.random.randint(0, i - 1, int(num_salt)))
          for i in img.shape]
out[coords] = 255

# Pepper mode
num_pepper = amount * img.size * (1. - s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_pepper))
          for i in img.shape]
out[coords] = 0

noisy = out

plt.subplot(2,2,1)
plt.imshow(noisy, 'gray')
plt.title('Salt and pepper noise')
plt.xticks([])
plt.yticks([])

avg = cv2.blur(noisy,(3,3))

plt.subplot(2,2,2)
plt.imshow(avg, 'gray')
plt.title('Averaging smoothing')
plt.xticks([])
plt.yticks([])

median = cv2.medianBlur(noisy, 3)
plt.subplot(2,2,3)
plt.imshow(median, 'gray')
plt.title('Median smoothing')
plt.xticks([])
plt.yticks([])

gaussian = cv2.GaussianBlur(noisy,(3,3),0.5)
plt.subplot(2,2,4)
plt.imshow(gaussian, 'gray')
plt.title('Gaussian smoothing')
plt.xticks([])
plt.yticks([])

plt.show()
