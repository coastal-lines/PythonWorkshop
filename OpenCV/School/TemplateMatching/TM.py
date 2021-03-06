import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv.imread(r'C:\Temp2\Flash\temp1.bmp')
templ = cv.imread(r'C:\Temp2\Flash\tmp1.bmp')



result = cv.matchTemplate(img, templ, cv.TM_CCOEFF)
