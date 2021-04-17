import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread(r'C:\Users\User\Desktop\Temp\New folder (5)\Clipboard01.jpg')
img2 = cv2.imread(r'C:\Users\User\Desktop\Temp\New folder (5)\Clipboard02.jpg')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

img1 = cv2.resize(img1, (640,480))
img2 = cv2.resize(img2, (640,480))

blended = cv2.addWeighted(src1=img1,alpha=0.9,src2=img2,beta=0.2,gamma=0)

plt.imshow(blended)
plt.show()