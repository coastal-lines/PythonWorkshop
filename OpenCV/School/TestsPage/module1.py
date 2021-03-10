import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

def validateText(img, text):
    textFromImage = pytesseract.image_to_string(img)
    if text in textFromImage:
        return True
    else:
        return False

img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')
crop_img = None

#findFilterTests
min = np.array([245, 245, 245])
max = np.array([255, 255, 255])
blur = cv.GaussianBlur(img, (3, 3), 0)
thresh = cv.inRange(blur, min, max)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    if w > 209 and h > 550:
        print(x,y,w,h)
        cv.drawContours(img, [cnt], 0, (0,255,0), 3)
        #crop_img = img[y:y+h, x:x+w]

#find Test Name and Test Reference fields
min = np.array([250, 250, 250])
max = np.array([255, 255, 255])
blur = cv.GaussianBlur(img, (3, 3), 0)
thresh = cv.inRange(blur, min, max)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    x,y,w,h = cv.boundingRect(cnt)
    d = math.sqrt(w**2 + h**2)
    if d > 216.0 and d < 219.0:
        print(x,y,w,h)
        print("d: " + str(d))
        y = y - 25
        h = h + 25
        x = x - 5
        w = w + 5
        crop_img = img[y:y+h, x:x+w]
        if validateText(crop_img, "Test Name") == True:
            print("Test Name")
        point1 = (x, y)
        point2 = (x + w, y + h)
        cv.rectangle(img, point1, point2, (0,255,0), 1)

#find Apply Filters button
img_gr = cv.imread(r'C:\Temp2\Flash\tests4.bmp', cv.IMREAD_GRAYSCALE)
template = cv.imread(r'C:\Temp2\Flash\tmp1.bmp', cv.IMREAD_GRAYSCALE)
h, w = template.shape
res = cv.matchTemplate(img_gr, template, cv.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
x = min_loc[0]
y = min_loc[1]
point1 = (x , y)
point2 = (x + w, y + h)
cv.rectangle(img, point1, point2, (0,255,0), 1)

cv.imshow('', img)
cv.waitKey(0)

"""
    def findTriangleByColor(roi, min, max, wUser, hUser):
        #min color
        min = np.array(min)
        #max color
        max = np.array(max)
    
        #remove some details by gaussian blur
        blur = cv.GaussianBlur(roi, (7, 7), 0)
        #remove other colors - min color and max color range
        thresh = cv.inRange(blur, min, max)

        #find contours
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        #find specific triangle by parameters
        for cnt in contours:
            x,y,w,h = cv.boundingRect(cnt)
            if w > wUser and h > hUser:
                print(x,y,w,h)
                cv.drawContours(img, [cnt], 0, (0,255,0), 3) # рисуем прямоугольник
                #return x,y,w,h

    def cutArea(img, x, y, w, h):
        crop_img = img[y:y+h, x:x+w]

        return crop_img

    def findFilterTests():
        #find FilterTests region
        w = img.shape[1]
        h = img.shape[0]
        roi = img[0:w,0:h]
        x,y,w,h = findTriangleByColor(roi, [245, 245, 245], [255, 255, 255], 209, 550)
        filterTests = cutArea(img, x, y, w, h)
        return filterTests, x, y, w, h

    def findF1(temp):
        #find FilterTests region
        w = temp[3]
        h = temp[4]
        roi = img[temp[1]:w, temp[2]:h]
        x,y,w,h = findTriangleByColor(roi, [245, 245, 245], [255, 255, 255], 215, 20)
        #F1 = cutArea(img, x, y, w, h)
        #return F1, x, y, w, h

    filterTests = findFilterTests()
    f1 = findF1(filterTests)

    cv.imshow('', img)
    cv.waitKey(0)
"""

#f=100