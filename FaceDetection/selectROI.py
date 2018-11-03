import cv2
import numpy as np

img=cv2.imread('group.jpg')


r=cv2.selectROI(img)
cropped=img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

cv2.imshow("Cropped", cropped)

cv2.imwrite('cropped.jpg', cropped)

c=cv2.waitKey(0)

if c==ord('q'):
    cv2.destroyAllWindows()
    