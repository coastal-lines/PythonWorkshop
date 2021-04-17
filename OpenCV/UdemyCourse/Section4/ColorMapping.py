import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r'C:\Users\User\Desktop\Temp\New folder (5)\Clipboard01.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
img = cv2.cvtColor(img,cv2.COLOR_RGB2HLS)

plt.imshow(img)
plt.show()