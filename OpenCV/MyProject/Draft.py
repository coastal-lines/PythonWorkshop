import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')

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

def edgeDetection():
    img_blur = imgBlur()
    edges = cv.Canny(img_blur, 100, 200)
    showImg(edges)

edgeDetection()