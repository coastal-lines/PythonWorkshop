import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'C:\Users\User\Desktop\Temp\New folder (5)\Clipboard01.jpg')
img2 = cv2.imread(r'C:\Users\User\Desktop\Temp\New folder (5)\Clipboard02.jpg')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

