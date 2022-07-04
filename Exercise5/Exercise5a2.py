import cv2
import matplotlib.pyplot as plt

path = 'Images/'

for i in range(15):
    img = cv2.imread(path + 'imagenes_botellas/botella_A_' + repr(i + 1) + '.bmp', 0)  # bottle A in red color
    Hm = cv2.HuMoments(cv2.moments(img, False)).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'ro')

    img = cv2.imread(path + 'imagenes_botellas/botella_B_' + repr(i + 1) + '.bmp', 0)  # bottle B in green color
    Hm = cv2.HuMoments(cv2.moments(img, False)).flatten()[0:2]
    plt.plot(Hm[0], Hm[1], 'go')

    img = cv2.imread(path + 'imagenes_botellas/botella_C_' + repr(i + 1) + '.bmp', 0)  # bottle C in blue color
    Hm = cv2.HuMoments(cv2.moments(img, False)).flatten()[0:2]
    plt.plot(Hm[0], Hm[1], 'bo')


plt.show()