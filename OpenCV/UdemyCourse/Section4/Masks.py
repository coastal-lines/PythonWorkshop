import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\dog_backpack.png')
img2 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\watermark_no_copy.png')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

