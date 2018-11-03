import numpy as np
import cv2


canvas= np.zeros((300,300,3), dtype="uint8")
cv2.imshow("Canvas", canvas)

cv2.waitKey(0)

color=(133, 200,190)
cv2.rectangle(canvas,(10,10), (60,60), color, 5)
cv2.imshow("Rectangle", canvas)

cv2.rectangle(canvas, (60,60), (200,200), color, -1)
cv2.imshow("Filled Rectangle", canvas)

cv2.waitKey(0)