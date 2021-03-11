from OpenCVMethods.FindGuiObjects import FindByOpenCVClass
import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Temp2\Flash\tests1.bmp')
min = np.array([245, 245, 245])
max = np.array([255, 255, 255])
width = 209
height = 550
FindByOpenCVClass.FindByColorSegmentation(img, min, max, width, height)