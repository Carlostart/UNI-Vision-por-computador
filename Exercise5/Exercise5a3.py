import cv2
import matplotlib.pyplot as plt
import numpy as np

path = '../Images/'

HmA = []
HmB = []
HmC = []

for i in range(15):
    img = cv2.imread(path + 'imagenes_botellas/botella_A_' + repr(i + 1) + '.bmp', 0)  # bottle A in red color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'ro')
    HmA.append([Hm[0],Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_B_' + repr(i + 1) + '.bmp', 0)  # bottle B in green color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'go')
    HmB.append([Hm[0], Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_C_' + repr(i + 1) + '.bmp', 0)  # bottle C in blue color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'bo')
    HmC.append([Hm[0], Hm[1]])

HmA = np.array(HmA)
HmB = np.array(HmB)
HmC = np.array(HmC)

plt.plot(float((sum(HmA[:, 0])) / len(HmA)), float((sum(HmA[:, 1])) / len(HmA)), 'kx')  # Now we do the average of the Hu Moments for the centroid
plt.plot(float((sum(HmB[:, 0])) / len(HmB)), float((sum(HmB[:, 1])) / len(HmB)), 'kx')  # for each bottle type and put it on the plot with a black X
plt.plot(float((sum(HmC[:, 0])) / len(HmC)), float((sum(HmC[:, 1])) / len(HmC)), 'kx')

plt.show()