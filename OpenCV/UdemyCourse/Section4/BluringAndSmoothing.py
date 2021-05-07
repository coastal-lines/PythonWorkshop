import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cv2.COLOR_BGR2RGB)
    plt.show()

img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\bricks.jpg').astype(np.float32) / 255

show_pic(img)