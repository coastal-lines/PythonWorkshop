import cv2
import numpy as np

img = cv2.imread(r'C:\Temp2\ForTesseract\ForKeras\edit_test_form_0.png')

width, height = img.shape[:2]
edges = cv2.Canny(img,width,height)
cv2.imshow('Edges',edges)