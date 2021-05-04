import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\rainbow.jpg',0)

#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\crossword.jpg',0)
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8)
show_pic(th2)


#plt.imshow(img)
#plt.show()

