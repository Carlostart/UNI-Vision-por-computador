import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read source image.
    path = 'Images/imagenes_homografias/'
    im_src = cv2.imread(path + 'long_jump_0.PNG')

    # Four corners of the stadium in source image
    pts_src = np.array([[622, 57],[566, 552],[146, 534],[472, 56]])

    # Four corners of the destine image
    pts_dst = np.array([[0,0], [0, 122], [30, 122], [30, 0]])

    # Calculate Homography
    matrix, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_src, matrix, (30, 122))

    # Search the mark of the line with the intensity of the grayscale image
    gray = cv2.cvtColor(im_out, cv2.COLOR_RGB2GRAY)
    h, w = gray.shape
    for width in range(0,w):
        if gray[2,width]<=100:
            print(width-1,'cm')
            break


    plt.imshow(gray,'gray')
    plt.title('homography')
    plt.show()