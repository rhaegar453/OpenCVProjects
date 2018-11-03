import numpy as np
import cv2


canvas= np.zeros((300,300,3), dtype="uint8")
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)

(centerX, centerY)=(canvas.shape[1]//2, canvas.shape[0]//2)

cv2.circle(canvas, (centerX,centerY),30, (0,255,0))
cv2.imshow("Circle", canvas)

for r in range(0,175,25):
    cv2.circle(canvas,(centerX, centerY),r,(255,0,0))


cv2.imshow("Concentric Circles", canvas)
cv2.waitKey(0)
