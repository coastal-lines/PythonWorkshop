import cv2 as cv
import numpy as np

img = cv.imread(r'c:\Temp2\ForTesseract\pic10.png')
ret, thresh = cv.threshold(img, 127, 255,0)
contours,hierarchy = cv.findContours(thresh,1)
cnt1 = contours[0]
contours,hierarchy = cv.findContours(thresh2,2,1)
cnt2 = contours[0]
ret = cv.matchShapes(cnt1,cnt2,1,0.0)
print( ret )