import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)

def translate(image, x, y):
    M=np.float32([[1,0,x],[0,1,y]])
    shifted=cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
    return shifted

shifted2=translate(image, x=70, y=-45)

cv2.imshow("Shifted", shifted2)
cv2.waitKey(0)
