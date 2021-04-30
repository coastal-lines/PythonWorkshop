import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\rainbow.jpg',0)

#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

plt.imshow(thresh1,cmap='gray')
plt.show()