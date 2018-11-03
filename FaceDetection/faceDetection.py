import cv2

image=cv2.imread('group.jpg')

gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
path='haarcascade_frontalface_default.xml'

face_cascade=cv2.CascadeClassifier(path)

faces=face_cascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=5, minSize=(40,40))
print(len(faces))

for (x,y, w, h) in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h),(0,255,0), 2)

cv2.imshow("Image", image)

cv2.waitKey(0)
