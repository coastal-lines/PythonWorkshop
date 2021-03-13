from OpenCVMethods.FindGuiObjects import FindByOpenCVClass
import cv2 as cv
import numpy as np
from GuiObject import GuiObject

filterTest = None

#find Tests->Filter Tests
def findFilterTest():
    img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')
    min = np.array([245, 245, 245])
    max = np.array([255, 255, 255])
    width = 247
    height = 565
    x, y, w, h = FindByOpenCVClass.FindByColorSegmentation(img, min, max, width, height)
    filterTest = GuiObject("FilterTest", "Tests", x, y, w, h)
    self.filterTest = filterTest
    return filterTest

def findTestNameOfFilterTest():
    filterTest = findFilterTest()
    
    min = np.array([250, 250, 250])
    max = np.array([255, 255, 255])
    width = 218
    height = 17
    text = "Test Name"



findTestNameOfFilterTest()
r=0