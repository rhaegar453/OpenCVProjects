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
blurred=cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("Blurred Image", blurred)

(T, thresholded)=cv2.threshold(image, 140, 255, cv2.THRESH_BINARY)


cv2.imshow("Thresholded", thresholded)

(T, Invthresholded)=cv2.threshold(image, 140, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Inverse Threshold", Invthresholded)

cv2.waitKey(0)
