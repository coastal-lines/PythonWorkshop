import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class Demo():
    filterTests = None

    #open image
    img = cv.imread(r'C:\Temp2\ForTesseract\pic.png')

    def findTrianglesByColor(self, roi, min, max, wUser, hUser):
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
                return x,y,w,h

    #find specific triangle coordinates by color segmentation
    def findTriangleByColor(self, roi, min, max, wUser, hUser):
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
                return x,y,w,h

    #cut subarea from image
    def cutArea(self, img, x, y, w, h):
        crop_img = img[y:y+h, x:x+w]

        return crop_img

    def findFilterTests(self):
        #find FilterTests region
        w = img.shape[1]
        h = img.shape[0]
        roi = img[0:w,0:h]
        x,y,w,h = findTriangleByColor(roi, [245, 245, 245], [255, 255, 255], 209, 550)
        self.filterTests = cutArea(img, x, y, w, h)

    def findTestNameField(self):
        #find FilterTests region
        w = img.shape[1]
        h = img.shape[0]
        roi = img[0:w,0:h]
        x,y,w,h = findTriangleByColor(roi, [255, 255, 255], [255, 255, 255], 215, 20)
        testNameField = cutArea(img, x, y, w, h)

d = Demo()
d.findFilterTests()
findTestNameField()
cv.imshow('', img)
cv.waitKey(0)