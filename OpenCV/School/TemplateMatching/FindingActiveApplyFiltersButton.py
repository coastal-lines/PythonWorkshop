import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

img = cv.imread(r'C:\Temp2\Flash\tests4.bmp')

# - поиск шаблона работает только для чб изображений
img_gr = cv.imread(r'C:\Temp2\Flash\tests4.bmp', cv.IMREAD_GRAYSCALE)
template = cv.imread(r'C:\Temp2\Flash\tmp1.bmp', cv.IMREAD_GRAYSCALE)

# - сохраняем ширину и высоту паттерна
h, w = template.shape

# - TM_SQDIFF метод квадратов разностей. Идеальное совпадение, если сумма квадратов разностей равна 0
res = cv.matchTemplate(img_gr, template, cv.TM_SQDIFF)

#min_val - минимум
#max_val - максимум
#min_loc - позиция (x,y) минимума
#max_loc - позиция (x, y) максимума
#нам нужен минимум - т.е. берем точку, в которой был найден минимум
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

# - получаем координаты и рисуем прямоугольник
x = min_loc[0]
y = min_loc[1]
point1 = (x , y)
point2 = (x + w, y + h)
cv.rectangle(img, point1, point2, (0,255,0), 1)

#threshold = 0.9
#loc = np.where( res >= threshold)

"""
for result in loc:
    x = min_loc[0]
    y = min_loc[1]
    point1 = (x , y)
    point2 = (x + w, y + h)
    cv.rectangle(img, point1, point2, (0,255,0), 1)
    #cv.rectangle(img, result, (result[0] + w, result[1] + h), (0,0,255), 1)
    #cv.rectangle(img, pt,      (pt[0], pt[1]), (0,0,255), 1)

#for pt in zip(*loc[::-1]):
 #   cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,0), 1)
"""

cv.imshow('', img)
cv.waitKey(0)