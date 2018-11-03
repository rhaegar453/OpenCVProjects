import cv2
import os

facePath="haarcascade_frontalface_default.xml"
faceCascade=cv2.CascadeClassifier(facePath)

def get_images():
    
    if not os.path.exists('database'):
        os.makedirs('database')
    
    pic_num=len(os.listdir('database/'))
    
    for files in ['source', 'source2']:
        for image in os.listdir(files):
            try:
                image_path=str(files)+'/'+str(image)
                image=cv2.imread(image_path)
                print(image.shape)
                gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                faces=faceCascade.detectMultiScale(gray, scaleFactor=1.10, minNeighbors=8, minSize=(40,40))
                
                for (x, y, w, h) in faces:
                    resized_image=image[y:y+h, x:x+w]
                    cv2.imwrite("database/"+str(pic_num)+".jpg", resized_image)

                
                pic_num+=1
                
                
                print("Successful")
            except Exception as e:
                print(str(e))
            
            
get_images()