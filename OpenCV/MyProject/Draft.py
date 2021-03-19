import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

def showImg(img):
    cv.imshow("", img)
    cv.waitKey(0)

def rgb2hsv():
    img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    showImg(img_hsv)

def rgb2lab():
    img_lab = cv.cvtColor(img, cv.COLOR_RGB2Lab)
    showImg(img_lab)

def rgb2gray():
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    #showImg(img_gray)
    return img_gray

def imgBlur():
    img_gray = rgb2gray()
    img_blur = cv.blur(img_gray, (3, 3))
    #showImg(img_blur)
    return img_blur

def imgThreshold(min, max):
    img = cv.imread(r'C:\Temp2\Flash\tests1.bmp', 0)
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
    ret, thresh1 = cv.threshold(img_gray, min, max, cv.THRESH_BINARY)
    #showImg(thresh1)

    return thresh1

def edgeDetection():
    img_blur = imgBlur()
    edges = cv.Canny(img_blur, 100, 150, L2gradient = True)
    showImg(edges)

def contourDetection(im):
    contours, hierarchy = cv.findContours(im, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x,y,w,h = cv.boundingRect(contour)
        point1 = (x , y)
        point2 = (x + w, y + h)
        cv.rectangle(img, point1, point2, (0,255,0), 1)

    cv.imshow("", img)
    cv.waitKey(0)

thr = imgThreshold(238, 240)
contourDetection(thr)
