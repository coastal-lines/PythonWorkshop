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
        imgCopy = CommonHelpMethodsClass.copyImage(self.img)
        obj = CommonHelpMethodsClass.loadJsonAnnotations("FilterTest")

        min = np.array([obj['minColor']])
        max = np.array([obj['maxColor']])
        width = obj['w']
        height = obj['h']
        x, y, w, h = FindByOpenCVClass.FindByColorSegmentation(imgCopy, min, max, width, height)
        cropArea = CommonHelpMethodsClass.cropImage(imgCopy, x, y, w, h)
        filterTest = GuiObject(obj['name'], obj['parent'], x, y, w, h, cropArea)

        return filterTest

    def findTestNameOfFilterTest(self):
        imgCopy = CommonHelpMethodsClass.copyImage(self.img)
        obj = CommonHelpMethodsClass.loadJsonAnnotations("Test Name")
        filterTest = self.findFilterTest()

        min = np.array([250, 250, 250])
        max = np.array([255, 255, 255])
        width = 218
        height = 17
        text = "Test Name"

        x, y, w, h = FindByOpenCVClass.FindByColorSegmentationAndName(filterTest.img, text, min, max, width, height)
        origX, origY = CommonHelpMethodsClass.findOriginalCoordinates(filterTest.x, filterTest.y, x, y)
        cropArea = CommonHelpMethodsClass.cropImage(imgCopy, origX, origY, w, h)
        testNameOfFilterTest = GuiObject("TestNameOfFilterTestField", "FilterTest", origX, origY, w, h, cropArea)

        return testNameOfFilterTest

    def findTestReferenceOfFilterTest(self):
        imgCopy = CommonHelpMethodsClass.copyImage(self.img)
        obj = CommonHelpMethodsClass.loadJsonAnnotations("Test Reference")
        filterTest = self.findFilterTest()
    
        min = np.array([250, 250, 250])
        max = np.array([255, 255, 255])
        width = 218
        height = 17
        text = "Test Reference"

        x, y, w, h = FindByOpenCVClass.FindByColorSegmentationAndName(filterTest.img, text, min, max, width, height)
        origX, origY = CommonHelpMethodsClass.findOriginalCoordinates(filterTest.x, filterTest.y, x, y)
        cropArea = CommonHelpMethodsClass.cropImage(imgCopy, origX, origY, w, h)
        testReferenceOfFilterTest = GuiObject("TestReverenceOfFilterTestField", "FilterTest", origX, origY, w, h, cropArea)

        return testReferenceOfFilterTest

def draw(obj, img):
    point1 = (obj.x, obj.y)
    point2 = (obj.x + obj.w, obj.y + obj.h)
    cv.rectangle(img, point1, point2, (0,255,0), 1)

#каждый раз на вход поиска нужно подавать новую копию - узнать почему
img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')

m = MainClass(img)
t = FindByOpenCVClass.findByContoursAndText(img, "Subject Name", 238, 240)
filterTest = m.findFilterTest()
testNameOfFilterTest = m.findTestNameOfFilterTest()
testReferenceOfFilterTest = m.findTestReferenceOfFilterTest()

"""
draw(filterTest, img)
draw(testNameOfFilterTest, img)
draw(testReferenceOfFilterTest, img)
CommonHelpMethodsClass.ShowImage(img)
"""


y=0