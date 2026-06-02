# openCV colors are BGR 

import cv2
import numpy as np
print(cv2.__version__)

while True:
    frame=np.zeros([250,250],dtype=np.uint8)
    color=1

    for i in range(50):
        for j in range(50):
            if(color==1):
                frame[i*5:(i+1)*5,j*5:(j+1)*5]=0
            if(color==0):
                frame[i*5:(i+1)*5,j*5:(j+1)*5]=255
            color^=1
        color^=1
                   
    
    
    cv2.imshow('Win', frame)
    cv2.moveWindow('Win',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
