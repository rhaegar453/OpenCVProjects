import numpy as np
import matplotlib.pyplot as plt
import cv2

image=cv2.imread("test.jpg")
image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.imshow(image)

cropped=image[400:550,400:600]
plt.imshow(cropped)