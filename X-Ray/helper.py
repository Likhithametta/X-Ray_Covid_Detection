# #Helper packages 
import tensorflow as tf
import numpy as np
import cv2

#decode the image
import base64

class Helper:
    def __init__(self) -> None:
        self.model = tf.keras.models.load_model('./models/Covid_Binary.h5')
        self.classes = ['COVID19 Pneumonia','Normal']  # covid== < 0.5 , normal== > 0.5

    def predict(self,bs4string) ->dict:
        '''
        :input -> base64 encoded string
        '''
        #decode image string and pre-processing
        img = base64.b64decode(bs4string)
        img = cv2.imdecode(np.fromstring(img,np.uint8), cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img,(150,150))
        img = img[np.newaxis, :,  :, :]
        img = img/255.0
        prob = self.model.predict(img)[0][0] # output from model example: [[0.9891]]
        res = dict()
        if prob > 0.5 : 
            res['cls'] = self.classes[1]
            res['acc'] = round(prob*100,2)
        else:
            res['cls'] = self.classes[0]
            res['acc'] = round((1-prob)*100,2)
        return res