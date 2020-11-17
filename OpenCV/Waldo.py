import cv2
import numpy as np
from matplotlib import pyplot as plt
import imutils

img = cv2.imread(r'c:\Temp2\ForTesseract\pic.png')
img2 = img.copy()
template = cv2.imread(r'c:\Temp2\ForTesseract\pic3.png')
w, h = template.shape[:2]

result = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF)
(_, _, minLoc, maxLoc) = cv2.minMaxLoc(result)

topLeft = maxLoc
botRight = (topLeft[0] + w, topLeft[1] + h)
roi = img2[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]

mask = np.zeros(img2.shape, dtype = "uint8")
puzzle = cv2.addWeighted(img2, 0.25, mask, 0.75, 0)

puzzle[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = roi
# display the images
cv2.imshow("Puzzle", imutils.resize(img, height = 650))
cv2.imshow("Waldo", template)
cv2.waitKey(0)