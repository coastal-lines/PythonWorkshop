import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread(r'c:\Temp2\ForTesseract\pic10.png', cv2.IMREAD_GRAYSCALE)
img2 = img.copy()
template = cv2.imread(r'c:\Temp2\ForTesseract\pic11.png', cv2.IMREAD_GRAYSCALE)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

cv2.imshow('Detected',img)
cv2.waitKey(0)