import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)
    
cv2.waitKey(0)


chans=cv2.split(image)
colors=("b","g","r")

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("No of pixels")

for (chan, color) in zip(chans, colors):
    hist=cv2.calcHist([chan],[0], None, [256], [0,256])
    plt.plot(hist)
    
plt.show()
cv2.waitKey(0)

