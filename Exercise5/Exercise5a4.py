import cv2
import matplotlib.pyplot as plt
import numpy as np

def distance(pt_1, pt_2):
    pt_1 = np.array((pt_1[0], pt_1[1]))
    pt_2 = np.array((pt_2[0], pt_2[1]))
    return np.linalg.norm(pt_1-pt_2)    # calculates the distance between 2 points

def closest_node(node, nodes):  # the node with less distance is the closest point
    pt = []
    dist = 9999999
    for n in nodes:
        if distance(node, n) <= dist:
            dist = distance(node, n)
            pt = n
    return pt

path = '../Images/'

HmA = []
HmB = []
HmC = []

for i in range(15):
    img = cv2.imread(path + 'imagenes_botellas/botella_A_' + repr(i + 1) + '.bmp', 0)  # bottle A in red color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2]  # Two first Hu moments
    HmA.append([Hm[0], Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_B_' + repr(i + 1) + '.bmp', 0)  # bottle B in green color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2]  # Two first Hu moments
    HmB.append([Hm[0], Hm[1]])

    img = cv2.imread(path + 'imagenes_botellas/botella_C_' + repr(i + 1) + '.bmp', 0)  # bottle C in blue color
    M = cv2.moments(img, False)
    Hm = cv2.HuMoments(M).flatten()[0:2]  # Two first Hu moments
    HmC.append([Hm[0], Hm[1]])

HmA = np.array(HmA)
HmB = np.array(HmB)
HmC = np.array(HmC)

a = (float((sum(HmA[:, 0])) / len(HmA)), float((sum(HmA[:, 1])) / len(HmA)))

b = (float((sum(HmB[:, 0])) / len(HmB)), float((sum(HmB[:, 1])) / len(HmB)))

c = (float((sum(HmC[:, 0])) / len(HmC)), float((sum(HmC[:, 1])) / len(HmC)))

plt.show()

file = input('name of the file?\n')
img = cv2.imread(path + 'imagenes_botellas/' + file, 0)
M = cv2.moments(img, False)
Hm = cv2.HuMoments(M).flatten()[0:2]  # Two first Hu moments

node = closest_node(Hm, [a, b, c])

if node == a:
    print('Bottle Type A')
elif node == b:
    print('Bottle Tyoe B')
elif node == c:
    print('Bottle Type C')

