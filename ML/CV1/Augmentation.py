import cv2 as cv
import numpy as np

img = cv.imread(r'C:\Temp2\ForTesseract\ForKeras\edit_test_form_0.png')
img_copy = img.copy()

width, height = img.shape[:2]

for i in range(1, 100):
    img_copy = cv.resize(img, (height + i, width + i), interpolation=cv.INTER_LANCZOS4)
    cv.imwrite(f'C:\Temp2\ForTesseract\ForKeras\edit_test_form_{i}.png', img_copy)

for i in range(101, 200):
    img_copy = cv.resize(img, (height - i, width - i), interpolation=cv.INTER_LANCZOS4)
    cv.imwrite(f'C:\Temp2\ForTesseract\ForKeras\edit_test_form_{i}.png', img_copy)