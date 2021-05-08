import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

def load_img():
    img = cv2.imread(r'C:\Users\User\Downloads\Computer-Vision-with-Python\DATA\bricks.jpg').astype(np.float32) / 255
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


img = load_img()

gamma = 1/4
result = np.power(img, gamma)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)

kernel = np.ones(shape=(5,5),dtype=np.float32)/25
print(kernel)

#show_pic(img)