import cv2
import matplotlib.pyplot as plt
import numpy as np

path = '../Images/'
img1 = cv2.imread(path + 'pepsi_left.tif')
im1 = img1.copy()
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread(path + 'pepsi_right.tif')
im2 = img2.copy()
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


def correlation_coefficient(patch1, patch2):
    product = np.mean((patch1 - patch1.mean()) * (patch2 - patch2.mean()))
    stds = patch1.std() * patch2.std()
    if stds == 0:
        return 0
    else:
        product /= stds
        return product




gray1 = np.float32(gray1)
gray2 = np.float32(gray2)

dst1 = cv2.goodFeaturesToTrack(gray1, 100000, 0.1, 10)
dst2 = cv2.goodFeaturesToTrack(gray2, 100000, 0.1, 10)

dst1 = np.int0(dst1)
dst2 = np.int0(dst2)

cols1, rows1, retval=img1.shape
cols2, rows2, retval=img2.shape
for corner in dst1:
    x, y = corner.ravel()
    cv2.circle(img1, (x, y), 5, 255)

for corner in dst2:
    x, y = corner.ravel()
    cv2.circle(img2, (x, y), 5, (255,0,255))

for corner1 in dst1:
    x1, y1 = corner1.ravel()
    if  8 < x1 < cols1-8 and 8 < y1 < cols1-8:
        max = 0
        xmax = 0
        ymax = 0
        correlations = []
        img1d = img1.copy()
        cv2.rectangle(img1d,(x1-8,y1-8),(x1+8,y1+8),(0,255,0),1)
        crop_img1 = gray1[y1 - 8:y1 + 8, x1 - 8:x1 + 8].copy()
        for corner2 in dst2:
            x2, y2 = corner.ravel()
            if 8 < x2 < cols1 - 8 and 8 < y2 < cols1 - 8:
                crop_img2 = gray2[y1 - 8:y1 + 8, x1 - 8:x1 + 8].copy()
                co = correlation_coefficient(crop_img1.ravel(),crop_img2.ravel())
                correlations.append(co)
                if co > max:
                    max = co
                    xmax = x2
                    ymax = y2
        cropf = im2[ymax - 8:ymax + 8, xmax - 8:xmax + 8].copy()
        img2d= img2.copy()
        print(correlations)
        cv2.rectangle(img2d,(xmax-8,ymax-8),(xmax+8,ymax+8),(0,255,0),1)

        plt.subplot(2,2,1)
        plt.imshow(img1d)
        plt.title('Keyponts detected in the left image')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(2,2,2)
        plt.imshow(img2d)
        plt.title('Keyponts detected in the right image')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(2,2,3)
        plt.imshow(cropf,'gray')
        plt.title('crop test')
        plt.xticks([])
        plt.yticks([])

        plt.show()