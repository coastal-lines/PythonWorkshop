import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'c:\Temp2\ForTesseract\pic.png',0)
img2 = img.copy()
template = cv2.imread(r'c:\Temp2\ForTesseract\pic2.png',0)
w, h = template.shape[::-1]

found = None

for scale in np.linspace(0.2, 1.0, 20)[::-1]:
    resized = imutils.resize(img, width = int(img.shape[1] * scale))
    r = img.shape[1] / float(resized.shape[1])
    if resized.shape[0] < h or resized.shape[1] < w: 
            break
    found = (maxVal, maxLoc, r) 

(_, maxLoc, r) = found 
(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r)) 
(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))

cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2) 

cv2.imwrite(r'c:\Temp2\ForTesseract\result.png',img)
