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
    self.filterTest = GuiObject("FilterTest", "Tests", x, y, w, h)

def findTestNameOfFilterTest():


findFilterTest()
r=0