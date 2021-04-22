import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\dog_backpack.png')
img2 = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\watermark_no_copy.png')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img2 = cv2.resize(img2, (600,600))

x_offset = 934 - 600
y_offset = 1401 - 600

rows,cols,chanels = img2.shape

roi = img1[y_offset:1401,x_offset:943]

img2gray = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)

mask_inv = cv2.bitwise_not(img2gray)

plt.imshow(mask_inv, cmap='gray')
plt.show()