from flask import Flask
from flask_cors import CORS
import cv2
import base64
import numpy as np

app=Flask('CVaaS')
CORS(app)


def cv_engine(img, operation):
    if operation=='grayscale':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return None

def read_image(image_data):
    image_data=base64.decodebytes(image_data)
    with open('temp_image.jpg', 'wb') as f:
        f.write(image_data)
        f.close()
        
    image=cv2.imread('temp_image.jpg')
    return image
def encode_image(image):
    ret, data=cv2.imencode('.jpg', image)
    return base64.b64encode(data)

    
