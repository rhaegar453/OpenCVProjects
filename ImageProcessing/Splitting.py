import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)
    
cv2.waitKey(0)

(B, G, R)=cv2.split(image)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)

cv2.waitKey(0)
    
merged=cv2.merge([B, G ,R])
cv2.imshow("Merged", merged)

cv2.waitKey(0)

zeros=np.zeros(image.shape[:2], dtype="uint8")
Red=cv2.merge([zeros, zeros, R])
Green=cv2.merge([zeros, G, zeros])
Blue=cv2.merge([B, zeros,zeros])

cv2.imshow("Blue Component", Blue)

cv2.imshow("Red Component", Red)

cv2.imshow("Green Component", Green)

cv2.waitKey(0)

