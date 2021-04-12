import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)
cv2.rectangle(blank_img, pt1=(384,5), pt2=(500,150), color=(0,255,0), thickness=10)
cv2.circle(img=blank_img,center=(200,200),radius=50,color=(255,0,0),thickness=-1) #thicknes=-1 for filling figure
cv2.line(blank_img,pt1=(0,0),pt2=(500,500),color=(100,50,204),thickness=2)



plt.imshow(blank_img)
plt.show()