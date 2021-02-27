import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Temp2\ForTesseract\pic.png')

min = np.array([245, 245, 245])
max = np.array([255, 255, 255])

thresh = cv.inRange(img, min, max)
result = cv.bitwise_and(img, img, mask=thresh)
blur = cv.GaussianBlur(result, (7, 7), 0)


contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for cnt in contours:
        rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
        box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
        box = np.int0(box) # округление координат
        cv.drawContours(img,[box],0,(255,0,0),2) # рисуем прямоугольник

cv.imshow('', blur)
cv.waitKey(0)

#img_bw_rgb = cv.cvtColor(image_original, cv.COLOR_BGR2RGB)

plt.imshow(thresh, cmap="gray")
imgplot = plt.imshow(result)
plt.show()