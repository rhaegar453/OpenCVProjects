import cv2

cap=cv2.VideoCapture('watch.mp4')
path='haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(path)


while True:
    ret, frame=cap.read()
    
    if ret==True:
        faces=face_cascade.detectMultiScale(frame,scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
        
        if len(faces)!=0:
            for (x,y, w, h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 2)
                cv2.imshow("Frame", frame)
        else:
            cv2.imshow("Frame", frame)
            

        if cv2.waitKey(33) == ord('q'):
            break
        

        
cap.release()
cv2.destroyAllWindows()
    
    
    