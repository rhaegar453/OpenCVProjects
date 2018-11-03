import cv2

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    
    cv2.putText(frame, "CognitAcademy", (100, 400), 7, 2, (0,0,255))
    cv2.imshow("Image",frame)
    
    c=cv2.waitKey(1)
    
    if c==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()