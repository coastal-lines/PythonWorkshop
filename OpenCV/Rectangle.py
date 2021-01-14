import cv2
import matplotlib.pyplot as plt
import numpy as np

#hsv_min = np.array((0, 54, 5), np.uint8)
#hsv_max = np.array((187, 255, 253), np.uint8)

path = r'C:\Temp2\ForTesseract\2.png'
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img_bw_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

median_intensity = np.median(img_bw_rgb)
lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(155, (1.0 + 0.33) * median_intensity))
img_canny = cv2.Canny(img_bw_rgb, lower_threshold, upper_threshold)

imgplot = plt.imshow(cnts)
figManager = plt.get_current_fig_manager()
figManager.window.showMaximized()
plt.show()

