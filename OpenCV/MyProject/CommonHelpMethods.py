import cv2 as cv
import numpy as np
import pyautogui
import pytesseract

class CommonHelpMethodsClass():

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
        return crop_img

    @staticmethod
    def validateText(img, text, whereItShouldBe, x, y, w, h):
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

    def ShowImage(img):
        cv.imshow('', TakeScreenshot())
        cv.waitKey(0)


    #cv.imshow('', TakeScreenshot())
    #cv.waitKey(0)