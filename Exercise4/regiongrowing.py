import numpy as np
import cv2

def get8n(x, y, shape):
    out = []
    maxx = shape[1]-1
    maxy = shape[0]-1

    #top left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top center
    outx = x
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #top right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y-1,0),maxy)
    out.append((outx,outy))

    #left
    outx = min(max(x-1,0),maxx)
    outy = y
    out.append((outx,outy))

    #right
    outx = min(max(x+1,0),maxx)
    outy = y
    out.append((outx,outy))

    #bottom left
    outx = min(max(x-1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom center
    outx = x
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    #bottom right
    outx = min(max(x+1,0),maxx)
    outy = min(max(y+1,0),maxy)
    out.append((outx,outy))

    return out

def region_growing(img, seed, toler):
    list = [] # list of points to check
    outimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    list.append((seed[0], seed[1])) # add the initial one
    processed = [] # list of processed points
    media = img[seed[0], seed[1]] # the value of the first point is the average
    while(len(list) > 0):
        pix = list[0]
        outimg[pix[0], pix[1]] = 255
        points_in_region = 0
        for coord in get8n(pix[0], pix[1], img.shape):
            if abs(img[coord[0], coord[1]] - media) < toler:
                points_in_region = points_in_region + 1
                media = (media * points_in_region + img[coord[0], coord[1]]) / (points_in_region + 1)
                outimg[coord[0], coord[1]] = (0,255,0)
                if not coord in processed:
                    list.append(coord)
                    processed.append(coord)
        list.pop(0)
        cv2.imshow("progress",outimg)     # with these two lines you can see an animation for the process
        cv2.waitKey(1)                    # the more high the number in this line, the more slow will be the animation
    return outimg

