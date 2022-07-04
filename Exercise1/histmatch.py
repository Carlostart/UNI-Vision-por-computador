import numpy as np
import cv2

def cumulative_histogram(hist):
    cum_hist = hist.copy()

    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i - 1] + cum_hist[i]

    return cum_hist

def hist_match(img, img_ref):
    height = img.shape[0]
    width = img.shape[1]
    pixels = width * height

    height_ref = img_ref.shape[0]
    width_ref = img_ref.shape[1]
    pixels_ref = width_ref * height_ref

    hist = cv2.calcHist([img],[0], None, [256], [0,255])
    hist_ref = cv2.calcHist([img_ref],[0], None, [256], [0,255])

    cum_hist = cumulative_histogram(hist)
    cum_hist_ref = cumulative_histogram(hist_ref)

    prob_cum_hist = cum_hist / pixels

    prob_cum_hist_ref = cum_hist_ref / pixels_ref

    K = 256
    new_values = np.zeros((K))

    for a in np.arange(K):
        j = K - 1
        while True:
            new_values[a] = j
            j = j - 1
            if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
                break

    for i in np.arange(height):
        for j in np.arange(width):
            a = img.item(i,j)
            b = new_values[a]
            img.itemset((i,j), b)

    return img