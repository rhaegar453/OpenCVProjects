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

blurred=np.hstack([
        cv2.bilateralFilter(image,5,25,30),
        cv2.bilateralFilter(image,7,34,40),
        cv2.bilateralFilter(image,9,40,50)        
        ])

cv2.imshow("Bilateral Blurring",blurred)


cv2.waitKey(0)

