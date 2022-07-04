import cv2
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

path = '../Images/'

HmA = []
HmB = []
HmC = []

for i in range(15):
    img = cv2.imread(path + 'imagenes_botellas/botella_A_' + repr(i + 1) + '.bmp', 0)  # bottle A in red color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'b*')
    HmA.append([Hm[0],Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_B_' + repr(i + 1) + '.bmp', 0)  # bottle B in green color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'rx')
    HmB.append([Hm[0], Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_C_' + repr(i + 1) + '.bmp', 0)  # bottle C in blue color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2] # Two first Hu moments
    plt.plot(Hm[0], Hm[1], 'lime', marker ='o')
    HmC.append([Hm[0], Hm[1]])

HmA = np.array(HmA)
HmB = np.array(HmB)
HmC = np.array(HmC)

def eigsorted(cov):
    vals, vecs = np.linalg.eigh(cov)
    order = vals.argsort()[::-1]
    return vals[order], vecs[:,order]

def error_ellipse(x,y, const, color):
    cov = np.cov(x, y)
    vals, vecs = eigsorted(cov)
    theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
    w, h = 2 * np.sqrt(vals)
    ell = Ellipse(xy=(np.mean(x), np.mean(y)),
                  width=w*const, height=h*const,
                  angle=theta, color='black')
    ell.set_facecolor('none')
    ell.set_edgecolor(color)
    return ell

ax = plt.subplot()

plt.plot(float((sum(HmA[:, 0])) / len(HmA)), float((sum(HmA[:, 1])) / len(HmA)), 'bs', markeredgecolor = 'k' )  # Now we do the average of the Hu Moments for the centroid
ax.add_artist(error_ellipse(HmA[:,0],HmA[:,1],5, 'blue'))

plt.plot(float((sum(HmB[:, 0])) / len(HmB)), float((sum(HmB[:, 1])) / len(HmB)), 'rs', markeredgecolor = 'k')  # for each bottle type and put it on the plot with a black X
ax.add_artist(error_ellipse(HmB[:,0],HmB[:,1],3,'red'))

plt.plot(float((sum(HmC[:, 0])) / len(HmC)), float((sum(HmC[:, 1])) / len(HmC)), 'lime', marker = 's', markeredgecolor = 'k')
ax.add_artist(error_ellipse(HmC[:,0],HmC[:,1],3,'lime'))

plt.show()