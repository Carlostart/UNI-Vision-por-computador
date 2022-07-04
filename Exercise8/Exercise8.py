import numpy as np
import cv2

mfwMatrix = np.matrix('0.5 0 0; 0 0.5 0; 0 0 1')    # Move foward 0.5 meters
print(mfwMatrix)

path = 'Images/'
imgdepth = cv2.imread(path + 'person_depth.png',0)
imgrgb = cv2.imread(path + 'person_rgb.png')

h, w, retval = imgrgb.shape

retval = cv2.rgbd.RgbdNormals_create(h, w, cv2.CV_64F, np.matrix('525 0 319.5, 0 525 239.5, 0 0 1'), window_size=5)
