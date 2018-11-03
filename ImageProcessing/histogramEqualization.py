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

image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale Image", image)


eq=cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))

cv2.waitKey(0)


cv2.waitKey(0)
