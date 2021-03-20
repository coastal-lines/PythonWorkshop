import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

arr = np.zeros(shape=(5,5))
arr[:,:] = 10
print(arr)

rndArray = np.random.randint(0, 100, size=(5,5))
print(rndArray)
print(rndArray.min())
print(rndArray.max())

#open image by PIL
img = Image.open(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\00-puppy.jpg')

#pil image to ndarray
pic_arr = np.asarray(img)
print(pic_arr.shape)

arr_copy = pic_arr.copy()
arr_copy[:,:,0]=0
arr_copy[:,:,1]=0

plt.imshow(arr_copy)
plt.show()

