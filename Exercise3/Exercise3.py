import cv2
import matplotlib.pyplot as plt
import numpy as np
import normxcorr2 as ncc

path = 'Images/'
img1 = cv2.imread(path + 'pepsi_left.tif')
im1 = img1.copy()
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = cv2.imread(path + 'pepsi_right.tif')
im2 = img2.copy()
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

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
    img1d = img1.copy()
    cv2.rectangle(img1d,(x1-8,y1-8),(x1+8,y1+8),(0,255,0),1)
    if  8 < x1 < cols1-8 and 8 < y1 < cols1-8:
        crop1 = gray1[y1 - 8:y1 + 8, x1 - 8:x1 + 8].copy()
        img2d= img2.copy()
        corr = ncc.normxcorr2(crop1,gray2)
        corr = corr[8:408,8:520]
        max = 0
        xmax = 0
        ymax = 0
        correlaciones = []
        cont =0
        for corner2 in dst2:
            x2, y2 = corner2.ravel()
            correlaciones.append(corr[y2,x2])
            cont+=1
            if max < (corr[y2,x2]):
                max = (corr[y2,x2])
                ymax = y2
                xmax = x2
                contmax = cont


        cv2.rectangle(img2d, (xmax - 8, ymax - 8), (xmax + 8, ymax + 8), (0, 255, 0), 1)
        crop = im2[ymax - 8:ymax + 8, xmax - 8:xmax + 8]

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
        plt.imshow(crop,'gray')
        plt.title('Template')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(2,2,4)
        plt.xlim([0,200])
        plt.scatter(range(0,correlaciones.__len__()),correlaciones,1,'r')
        # plt.annotate('*', xy=(correlaciones.index(max)-3,max-0.075), xytext=(correlaciones.index(max)-3,max-0.075),color='green')

        plt.plot(contmax,corr[ymax,xmax],'gx')

        plt.show()