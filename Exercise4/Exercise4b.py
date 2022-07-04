import numpy as np
import cv2
import matplotlib.pyplot as plt

path = 'Images/'
img = cv2.imread(path + 'torre_monica.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# ------------------ COLOR ------------------------

Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res = res.reshape((img.shape))

# --------------- GRAY -----------------------------

Z = img_gray.reshape((-1,1))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
resgray = center[label.flatten()]
resgray = resgray.reshape((img_gray.shape))

plt.subplot(2,2,1)
plt.imshow(img)
plt.title('Color Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,2)
plt.imshow(res)
plt.title('Segmentation from color')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,3)
plt.imshow(img_gray,'gray')
plt.title('Gay Image')
plt.xticks([])
plt.yticks([])

plt.subplot(2,2,4)
plt.imshow(resgray,'gray')
plt.title('Segmentation from gray')
plt.xticks([])
plt.yticks([])

plt.show()