import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv.imread(r'C:\Temp2\Flash\temp1.bmp')
b,g,r = (img[300, 300])
i=0
