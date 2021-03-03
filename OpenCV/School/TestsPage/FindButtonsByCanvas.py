import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv.imread(r'C:\Temp2\Flash\tests4.bmp')

def validateText(img, text):
    textFromImage = pytesseract.image_to_string(img)
    if text in textFromImage:
        return True
    else:
        return False

ratio = 3
kernel_size = 3
src_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
low_threshold =30
img_blur = cv.blur(src_gray, (1,1))
detected_edges = cv.Canny(img_blur, low_threshold, low_threshold*ratio, kernel_size, L2gradient=True)
contours, hierarchy = cv.findContours(detected_edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    #print(x,y,w,h)
    d = math.sqrt(w**2 + h**2)
    if d > 226.0 and d < 226.9:
        print(d)
        crop_img = img[y:y+h, x:x+w]
        if validateText(crop_img, "Apply") == True:
            point1 = (x, y)
            point2 = (x + w, y + h)
            cv.rectangle(img, point1, point2, (0,255,0), 3)

cv.imshow("", img)
cv.waitKey(0)