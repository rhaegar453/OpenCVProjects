import numpy as np
import argparse
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="Path to the image")
args=vars(ap.parse_args())


image=cv2.imread(args["image"])
cv2.imshow("Original",image)


cv2.waitKey(0)

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim=None
    (h,w)=image.shape[:2]
    
    if width is None and height is None:
        return image
    
    if width is None:
        r=height/float(h)
        dim=(int(w*r), height)
        
    else:
        r=width/float(w)
        dim=(width/int(h*r))
        
    resized=cv2.resize(image, dim, interpolation=inter)
    return resized

image2=resize(image,height=400)
cv2.imshow("Resized(Height)", image2)

cv2.waitKey(0)
