import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#open image
img = cv.imread(r'C:\Temp2\ForTesseract\pic.png')

#find specific triangle coordinates by color segmentation
def findFilterTestsPosition(img, min, max):
    #min color
    min = np.array(min)
    #max color
    max = np.array(max)
    
    #remove some details by gaussian blur
    blur = cv.GaussianBlur(img, (7, 7), 0)
    #remove other colors - min color and max color range
    thresh = cv.inRange(blur, min, max)

    #find contours
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #find specific triangle by parameters
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        if w > 209 and h > 550:
            print(x,y,w,h)
            cv.drawContours(img, [cnt], 0, (0,255,0), 3) # рисуем прямоугольник
            return x,y,w,h

#cut subarea from image
def cutArea(img, x, y, w, h):
    crop_img = img[y:y+h, x:x+w]

    return crop_img

#find FilterTests region
x,y,w,h = findFilterTestsPosition(img, [245, 245, 245], [255, 255, 255])
newImg = cutArea(img, x, y, w, h)



cv.imshow('', newImg)
cv.waitKey(0)