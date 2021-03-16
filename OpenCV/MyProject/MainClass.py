from OpenCVMethods.FindGuiObjects import FindByOpenCVClass
from CommonHelpMethods import CommonHelpMethodsClass
from GuiObject import GuiObject
import cv2 as cv
import numpy as np

#it should be only one class for business

class MainClass():
    def __init__(self, img):
        self.img = img

    #find Tests->Filter Tests
    def findFilterTest(self):
        min = np.array([245, 245, 245])
        max = np.array([255, 255, 255])
        width = 247
        height = 565
        x, y, w, h = FindByOpenCVClass.FindByColorSegmentation(self.img, min, max, width, height)
        cropArea = CommonHelpMethodsClass.cropImage(self.img, x, y, w, h)
        filterTest = GuiObject("FilterTest", "Tests", x, y, w, h, cropArea)

        return filterTest

    def findTestNameOfFilterTest(self):
        filterTest = self.findFilterTest()
    
        min = np.array([250, 250, 250])
        max = np.array([255, 255, 255])
        width = 218
        height = 17
        text = "Test Name"

        x, y, w, h = FindByOpenCVClass.FindByColorSegmentationAndName(filterTest.img, text, min, max, width, height)
        origX, origY = CommonHelpMethodsClass.findOriginalCoordinates(filterTest.x, filterTest.y, x, y)
        cropArea = CommonHelpMethodsClass.cropImage(self.img, origX, origY, w, h)
        testNameOfFilterTest = GuiObject("TestNameOfFilterTestField", "FilterTest", origX, origY, w, h, cropArea)

        return testNameOfFilterTest

    def findTestReferenceOfFilterTest(self):
        filterTest = self.findFilterTest()
    
        min = np.array([250, 250, 250])
        max = np.array([255, 255, 255])
        width = 218
        height = 17
        text = "Test Reference"

        x, y, w, h = FindByOpenCVClass.FindByColorSegmentationAndName(filterTest.img, text, min, max, width, height)
        origX, origY = CommonHelpMethodsClass.findOriginalCoordinates(filterTest.x, filterTest.y, x, y)
        cropArea = CommonHelpMethodsClass.cropImage(self.img, origX, origY, w, h)
        testReferenceOfFilterTest = GuiObject("TestReverenceOfFilterTestField", "FilterTest", origX, origY, w, h, cropArea)

        return testReferenceOfFilterTest

img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')

#каждый раз на вход поиска нужно подавать новую копию - узнать почему
CommonHelpMethodsClass.loadJsonAnnotations()

imgCopy = CommonHelpMethodsClass.copyImage(img)
m = MainClass(imgCopy)

filterTest = m.findFilterTest()
filterTest2 = m.findFilterTest()
CommonHelpMethodsClass.copyImage(img)
testNameOfFilterTest = m.findTestNameOfFilterTest()
testReferenceOfFilterTest = m.findTestReferenceOfFilterTest()

y=0