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

image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blurred Image", blurred)

thresh=cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,15, 3)
cv2.imshow("Adaptive Threshold", thresh)

cv2.waitKey(0)
