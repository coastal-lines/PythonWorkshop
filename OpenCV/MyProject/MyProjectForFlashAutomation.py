import cv2 as cv
import numpy as np
import pyautogui

def TakeScreenshot():
    screenshot = pyautogui.screenshot()
    brgImg = np.array(screenshot)
    rgbImg = cv.cvtColor(brgImg, cv.COLOR_BGR2RGB)
    return rgbImg
















cv.imshow('', TakeScreenshot())
cv.waitKey(0)