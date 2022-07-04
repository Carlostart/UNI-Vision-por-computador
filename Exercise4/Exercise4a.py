import cv2
import matplotlib.pyplot as plt
import regiongrowing as rg

path = 'Images/'

img = cv2.imread(path+'rice.tif', 0)

x = input('x = ')
y = input('y = ')

mask = rg.region_growing(img, [int(x), int(y)], 20)

# Input image
plt.imshow(mask, 'gray')
plt.title('mask')
plt.xticks([])
plt.yticks([])
plt.show()
