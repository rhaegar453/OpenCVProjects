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
        cv2.medianBlur(image,3),
        cv2.medianBlur(image,5),
        cv2.medianBlur(image,7)
        ])
cv2.imshow("Blurred",blurred)

cv2.waitKey(0)

