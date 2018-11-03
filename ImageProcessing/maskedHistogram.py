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

mask=np.zeros(image.shape[:2], dtype="uint8")
(centerX, centerY)=(image.shape[1]//2, image.shape[0]//2)

rectangle=cv2.rectangle(mask, (centerX-100, centerY-100), (centerX+100, centerY+100), 255, -1)
cv2.imshow("Rectangle",rectangle)

cv2.waitKey(0)
for (chan, color) in zip(chans, colors):
    hist=cv2.calcHist([chan],[0],mask, [256], [0,256])
    plt.plot(hist)
    
plt.show()
cv2.waitKey(0)

