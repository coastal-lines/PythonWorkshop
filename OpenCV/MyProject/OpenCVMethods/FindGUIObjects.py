import cv2 as cv
import numpy as np

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
        for contour in contours:
            x, y, w, h = cv.boundingRect(contour)
            #if (w > width and w < width + shiftW) and (h > 550 and h < height + shiftH):
            if w > 209 and h > 550:
                print(x, y, w, h)
                cv.drawContours(img, [contour], 0, (0,255,0), 3)

        FindByOpenCVClass.ShowImage(img)

    #find by edges


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

    @staticmethod
    def ShowImage(img):
        cv.imshow('', img)
        cv.waitKey(0)