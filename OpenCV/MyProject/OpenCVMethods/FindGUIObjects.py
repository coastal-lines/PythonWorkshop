import cv2 as cv
import numpy as np
from CommonHelpMethods import CommonHelpMethodsClass

class FindByOpenCVClass():
    #find by color segmentation
    @staticmethod
    def FindByColorSegmentation(img, minColor, maxColor, width, height):
        shiftW = 5
        shiftH = 5
        min = np.array([245, 245, 245])
        max = np.array([255, 255, 255])
        blur = cv.GaussianBlur(img, (3, 3), 0)
        thresh = cv.inRange(blur, min, max)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        x, y, w, h = -1,-1,-1,-1
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if (w > width - shiftW and w < width + shiftW) and (h > h - shiftH  and h < h + shiftH):
                print(x, y, w, h)
                cv.drawContours(img, [contour], 0, (0,255,0), 3)
                break
        #FindByOpenCVClass.ShowImage(img)
        return x, y, w, h

    #find by color segmentation and name
    @staticmethod
    def FindByColorSegmentationAndName(img, text, minColor, maxColor, width, height):
        shiftW = 5
        shiftH = 5
        min = minColor
        max = maxColor
        blur = cv.GaussianBlur(img, (3, 3), 0)
        thresh = cv.inRange(blur, min, max)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        x, y, w, h = -1, -1, -1, -1
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            if (w > width - shiftW and w < width + shiftW) and (h > h - shiftH  and h < h + shiftH):
                if CommonHelpMethodsClass.validateText(img, text, x, y, w, h) == True:
                    print("Text is: " + text)
                    print(x, y, w, h)
                    cv.drawContours(img, [contour], 0, (0,255,0), 3)
                    break
        #FindByOpenCVClass.ShowImage(img)
        return x, y, w, h

    #find by pattern
    def FindbyImagePattern(img):
        orig_img = img

        # - поиск шаблона работает только для чб изображений
        img_gr = cv.imread(r'C:\Temp2\Flash\tests4.bmp', cv.IMREAD_GRAYSCALE)
        template = cv.imread(r'C:\Temp2\Flash\tmp1.bmp', cv.IMREAD_GRAYSCALE)

        # - сохраняем ширину и высоту паттерна
        h, w = template.shape

        # - TM_SQDIFF метод квадратов разностей. Идеальное совпадение, если сумма квадратов разностей равна 0
        res = cv.matchTemplate(img_gr, template, cv.TM_SQDIFF)

        #min_val - минимум
        #max_val - максимум
        #min_loc - позиция (x,y) минимума
        #max_loc - позиция (x, y) максимума
        #нам нужен минимум - т.е. берем точку, в которой был найден минимум
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

        # - получаем координаты и рисуем прямоугольник
        x = min_loc[0]
        y = min_loc[1]
        point1 = (x , y)
        point2 = (x + w, y + h)
        cv.rectangle(img, point1, point2, (0,255,0), 1)

        return point1, point2

    def findByContoursAndText(img, text, minThreshold, maxThreshold):
        imgCopy = CommonHelpMethodsClass.copyImage(img)
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
        ret, thresh1 = cv.threshold(img_gray, minThreshold, maxThreshold, cv.THRESH_BINARY)
        contours, hierarchy = cv.findContours(thresh1, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x,y,w,h = cv.boundingRect(contour)
            point1 = (x , y)
            point2 = (x + w, y + h)
            #ONLY FOR DEBUG
            if (w > 300 and h > 300) and (w < 1600):
                crop = CommonHelpMethodsClass.cropImage(img, x, y, w, h)
                actualText = CommonHelpMethodsClass.getTextFromImage(crop)
                print(actualText)
                cv.rectangle(img, point1, point2, (0,255,0), 1)
                if text in actualText:
                    cv.rectangle(img, point1, point2, (0,255,0), 1)
                    return x,y,w,h

        #FindByOpenCVClass.ShowImage(img)
            #break

    def findContoursByThreshold(img, minThreshold, maxThreshold):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_RGB2GRAY)
        ret, thresh1 = cv.threshold(img_gray, minThreshold, maxThreshold, cv.THRESH_BINARY)
        contours, hierarchy = cv.findContours(thresh1, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
        return contours, hierarchy

    def findContoursByMinMaxColors(img, min, max):
        imgCopy = CommonHelpMethodsClass.copyImage(img)
        min = np.array(min)
        max = np.array(max)
        blur = cv.GaussianBlur(imgCopy, (9, 9), 0)
        thresh = cv.inRange(blur, min, max)
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        return contours

    def getPointsFromContour(contour):
        x, y, w, h = cv.boundingRect(contour)
        point1 = (x , y)
        point2 = (x + w, y + h)
        return point1, point2

