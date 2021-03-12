import cv2 as cv
import numpy as np
import pyautogui

def TakeScreenshot():
    screenshot = pyautogui.screenshot()
    brgImg = np.array(screenshot)
    rgbImg = cv.cvtColor(brgImg, cv.COLOR_BGR2RGB)
    return rgbImg

def TakeCentrOfElement(pointLeftAbove, pointRightBottom):
    x1, y1 = pointLeftAbove[::]
    x2, y2 = pointRightBottom[::]
    centrX = ((x2 - x1) / 2) + x1
    centrY = ((y2 - y1) / 2) + y1
    return centrX, centrY

def CropImage(img, x, y, w, h):
    crop_img = img[y:y+h, x:x+w]
    return crop_img

def ShowImage(img):
    cv.imshow('', TakeScreenshot())
    cv.waitKey(0)


#cv.imshow('', TakeScreenshot())
#cv.waitKey(0)