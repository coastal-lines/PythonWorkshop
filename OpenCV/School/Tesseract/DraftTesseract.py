import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv.imread(r'C:\Temp2\Flash\TesseractTest\Clipboard03.bmp')
textFromImage = pytesseract.image_to_string(img)
i=0