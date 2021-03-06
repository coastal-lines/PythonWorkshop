import cv2 as cv
import numpy as np
import pyautogui
import pytesseract
import json

class CommonHelpMethodsClass():

    jsonData = None

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

    @staticmethod
    def cropImage(img, x, y, w, h):
        crop_img = img[y:y+h, x:x+w]
        #print("I'm cropping" + " " + str(x))
        return crop_img

    @staticmethod
    def validateText(img, text, x, y, w, h, whereItShouldBe = "top"):
        crop_img = None

        #make crop from main image firstly
        if whereItShouldBe == "top":
            x = x - 5
            y = y - 25
            h = h + 25
            w = w + 5
            crop_img = CommonHelpMethodsClass.cropImage(img, x, y, w, h)

        #try to find text in cropped image secondly
        textFromImage = pytesseract.image_to_string(crop_img)
        if text in textFromImage:
            return True
        else:
            return False

    @staticmethod
    def getTextFromImage(cropImg):
        textFromImage = pytesseract.image_to_string(cropImg)
        return textFromImage

    @staticmethod
    def findOriginalCoordinates(originalImgX, originalImgY, cropX, cropY):
        x = originalImgX + cropX
        y = originalImgY + cropY
        return x, y

    #@staticmethod
    def copyImage(img):
        return img.copy()

    def ShowImage(img):
        cv.imshow('', img)
        cv.waitKey(0)

    @staticmethod
    def loadJsonAnnotations(userObject):
        with open('C:\Temp2\Flash\labelimg\my.json') as f:
            jsonData = json.load(f)

        for obj in jsonData['guiObjects']:
            if obj['name'] == userObject:
                return obj



    #cv.imshow('', TakeScreenshot())
    #cv.waitKey(0)