import cv2
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())

image=cv2.imread(args["image"])
cv2.imshow("Image",image)

print("Height: {} pixels".format(image.shape[0]))
print("Width: {} pixels".format(image.shape[1]))
print("Channels: {} pixels".format(image.shape[2]))

cv2.waitKey(0)