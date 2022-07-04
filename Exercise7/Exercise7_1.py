import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read source image.
    path = 'Images/imagenes_homografias/'
    im_src = cv2.imread(path + 'bernabeu.jpg')

    # Four corners of the stadium in source image
    pts_src = np.array([[517, 254], [837, 291], [751, 663],[115, 462]])

    # Four corners of the destine image
    pts_dst = np.array([[0,0], [0, 300], [500, 300], [500, 0]])

    # Calculate Homography
    matrix, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination based on homography
    print(matrix)
    im_out = cv2.warpPerspective(im_src, matrix, (500, 300))

    plt.imshow(im_out)
    plt.title('homography')
    plt.show()