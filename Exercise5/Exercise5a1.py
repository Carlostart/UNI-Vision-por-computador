import cv2

path = '../Images/'
img = cv2.imread(path + 'imagenes_botellas/botella_A_1.bmp',0)

M = cv2.moments(img, False) # OpenCV has the function moments, which calculate the moments. The second parameter is True if the img is binary
# print(M)

print('mu00 = ',  M['m00'])
print('mu01 = 0')
print('mu10 = 0')
print('mu11 = ',M['mu11'])
print('mu20 = ',M['mu20'])
print('mu02 = ',M['mu02'])
print('mu21 = ',M['mu21'])
print('mu12 = ',M['mu12'])
print('mu30 = ',M['mu30'])
print('mu03 = ',M['mu03'])

# def mom(i,j,im):  # manual method
#     cols, rows= im.shape
#     mu = 0
#     for y in range(cols):
#         for x in range(rows):
#             mu = mu + ((y+1 - (sum(img[y]) / len(img[y])))**i)  * ((y+1 - (sum(img[:cols,x]) / len(img[:cols,x])))**j) * img[y,x]  # Central moments expression from the docx
#     print(mu)
#
# mom(2,0,img)