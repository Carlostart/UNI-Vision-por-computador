import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Read source image.
    path = 'Images/imagenes_homografias/'
    im_src = cv2.imread(path + 'bernabeu.jpg')
    im_src = cv2.cvtColor(im_src, cv2.COLOR_RGB2BGR)
    im_chiq = cv2.imread(path + 'chiquito3.jpg')
    im_chiq = cv2.cvtColor(im_chiq, cv2.COLOR_RGB2BGR)


    # Four corners of the stadium in source image
    pts_src = np.array([[517, 254], [837, 291], [751, 663],[115, 462]])

    # Four corners of the image of chiquito
    pts_dst = np.array([[0,0], [0, 360], [480, 360], [480, 0]])

    # Calculate Homography
    matrix, status = cv2.findHomography(pts_dst, pts_src)

    # Warp source image to destination based on homography
    im_out = cv2.warpPerspective(im_chiq, matrix, (1024, 768))

    # Convert the image into grayscale
    img2gray = cv2.cvtColor(im_out, cv2.COLOR_BGR2GRAY)
    # Make a mask with a theshold of 1
    ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)
    # And the inverse mask for the stadium
    mask_inv = cv2.bitwise_not(mask)
    # Add the stadium with its mask
    img1_bg = cv2.bitwise_and(im_src, im_src, mask=mask_inv)
    # And chiquito with its mask
    img2_fg = cv2.bitwise_and(im_out, im_out, mask=mask)
    # And at the end put the two parts together
    dst = cv2.add(img1_bg, img2_fg)

    plt.imshow(dst)
    plt.title('homography')
    plt.show()