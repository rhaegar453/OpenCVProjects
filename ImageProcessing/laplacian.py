import numpy as np
import argparse
import cv2


ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True)
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey", image)

lap=cv2.Laplacian(image,cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)
