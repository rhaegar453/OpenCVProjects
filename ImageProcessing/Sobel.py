import numpy as np
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True)
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", image)


SobelX=cv2.Sobel(image, cv2.CV_64F, 1, 0)
SobelY=cv2.Sobel(image, cv2.CV_64F, 0, 1)


SobelX=np.uint8(np.absolute(SobelX))
SobelY=np.uint8(np.absolute(SobelY))

SobelCombined=cv2.bitwise_or(SobelX, SobelY)

cv2.imshow("Sobel X", SobelX)
cv2.imshow("Sobel Y", SobelY)
cv2.imshow("Sobel Combined", SobelCombined)

cv2.waitKey(0)
