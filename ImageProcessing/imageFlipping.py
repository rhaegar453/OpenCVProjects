import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)

cv2.waitKey(0)

flippedH=cv2.flip(image,1)
flippedV=cv2.flip(image,0)
flippedHV=cv2.flip(image,-1)

cv2.imshow("Flipped Horizontally", flippedH)
cv2.imshow("Flipped Vertically", flippedV)
cv2.imshow("Flipped Horizontally and Vertically", flippedHV)

cv2.waitKey(0)


