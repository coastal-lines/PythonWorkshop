import cv2
import numpy as np
import matplotlib.pyplot as plt

blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)
font = cv2.FONT_HERSHEY_SIMPLEX
#org: bottom-left corner of the text string in the image
cv2.putText(img=blank_img,text='Hello',org=(10,500),fontFace=font,fontScale=4,color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)

#draw a polygon
blank_img = np.zeros(shape=(512,512,3), dtype=np.int16)
vertices = np.array([[100,300],[200,200],[400,300],[200,400]], dtype=np.int32)
pts = vertices.reshape((-1,1,2))
cv2.polylines(img=blank_img, pts=[pts],isClosed=True,color=(255,0,0),thickness=5)


plt.imshow(blank_img)
plt.show()