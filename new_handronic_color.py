from keras.models import load_model
import tensorflow as tf 

import keras
import cv2
import numpy as np

from keras.models import load_model

cap = cv2.VideoCapture(0)


#model = tf.keras.models.load_model()

model = load_model("handronic_4_10g.h5")
while True:
    

    ret,frame = cap.read()

    #frame = cv2.imread("photos\mug.JPG")
    frame = cv2.resize(frame, (400,300) )


    model_frame = cv2.resize(frame , (100,100) )
    #model_frame = cv2.cvtColor(model_frame, cv2.COLOR_BGR2GRAY)


    model_frame = model_frame.reshape(1, 100, 100,3)
    
    model_frame = np.array(model_frame,dtype="float16")/255
    
    output = model.predict(model_frame)
    output_class = np.argmax(output)
    
    cv2.putText(frame,str(output_class),(0,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    print(output)

    cv2.imshow("frame",frame)
    key = cv2.waitKey(1)& 0xFF
    if key == ord("q"):
            break

            
cv2.destroyAllWindows()
