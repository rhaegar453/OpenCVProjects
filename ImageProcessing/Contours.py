import numpy as np
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True)
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", image)

blurred=cv2.GaussianBlur(image, (3,3), 0)
cv2.imshow("Blurred", blurred)

canny=cv2.Canny(blurred, 30, 150)
cv2.imshow("Canny", canny)

(_,counts,_)=cv2.findContours(canny.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("The number of countours in the image is {}".format(len(counts)))

coins=image.copy()
cv2.drawContours(coins, counts, -1, (0,0,0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)
