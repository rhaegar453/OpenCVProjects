import numpy as np
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True)
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", image)

blurred=cv2.GaussianBlur(image, (5,5),0)
cv2.imshow("Blurred", blurred)

canny=cv2.Canny(blurred,30,150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)