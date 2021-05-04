import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\crossword.jpg',0)