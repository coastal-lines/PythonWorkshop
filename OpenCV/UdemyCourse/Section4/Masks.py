import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\dog_backpack.png')
img2 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\watermark_no_copy.png')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600,600))

#start point for mask
x_offset = 934 - 600
y_offset = 1401 - 600

#rows,cols,chanels = img2.shape

#Region of Interest (ROI)
roi = img1[y_offset:1401,x_offset:943]

img2gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

#inverse all bits
mask_inv = cv2.bitwise_not(img2gray)

#create white background by numpy
white_background = np.full(img2.shape,255,dtype=np.uint8)

#Дизьюнкция. Т.е. там где белый, применяем маску
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)

#?????
fg = cv2.bitwise_or(img2,img2,mask=mask_inv)

#????
final_roi = cv2.bitwise_or(roi,fg)

large_img = img1
small_img = final_roi

large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img



plt.imshow(img2)
plt.show()