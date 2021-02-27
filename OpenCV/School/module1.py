import cv2 as cv
import matplotlib.pyplot as plt

image_original = cv.imread(r'C:\Temp2\ForTesseract\pic.png')
img_bw_rgb = cv.cvtColor(image_original, cv.COLOR_BGR2RGB)

imgplot = plt.imshow(img_bw_rgb[0:100])
plt.show()