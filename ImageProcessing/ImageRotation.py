import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)


def rotate(image, angle, center=None, scale=1.0):
    (h,w)=image.shape[:2]
    
    
    if center is None:
        center=(w//2, h//2)
    
    M=cv2.getRotationMatrix2D(center,angle, scale)
    rotate=cv2.warpAffine(image,M,(w,h))
    return rotate

rotate2=rotate(image, -60)

cv2.imshow("Rotated", rotate2)

cv2.waitKey(0)
