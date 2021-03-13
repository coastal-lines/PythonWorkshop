from OpenCVMethods.FindGuiObjects import FindByOpenCVClass
from CommonHelpMethods import CommonHelpMethodsClass
from GuiObject import GuiObject
import cv2 as cv
import numpy as np

class MainClass():
    filterTest = None
    img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')


    #find Tests->Filter Tests
    def findFilterTest(self):
        #img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')
        min = np.array([245, 245, 245])
        max = np.array([255, 255, 255])
        width = 247
        height = 565
        x, y, w, h = FindByOpenCVClass.FindByColorSegmentation(img, min, max, width, height)
        cropArea = CommonHelpMethodsClass.cropImage(img, x, y, w, h)
        filterTest = GuiObject("FilterTest", "Tests", x, y, w, h, cropArea)
        #self.filterTest = filterTest
        return filterTest

    def findTestNameOfFilterTest(self):
        filterTest = self.findFilterTest(self)
    
        min = np.array([250, 250, 250])
        max = np.array([255, 255, 255])
        width = 218
        height = 17
        text = "Test Name"

        tempObj = FindByOpenCVClass.FindByColorSegmentationAndName(filterTest.img, text, min, max, width, height)
        origX, origY = CommonHelpMethodsClass.findOriginalCoordinates(self.img, cropX, cropY)
        return testNameOfFilterTest

m = MainClass
filterTest = m.findTestNameOfFilterTest(m)

y=0