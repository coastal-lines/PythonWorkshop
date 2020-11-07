import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'c:\Temp2\ForTesseract\pic.png',0)
img2 = img.copy()
template = cv2.imread(r'c:\Temp2\ForTesseract\pic3.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
threshold = 1
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imwrite(r'c:\Temp2\ForTesseract\result.png',img)