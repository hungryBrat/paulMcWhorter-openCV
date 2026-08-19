import cv2
print(cv2.__version__)

wd= 640
ht= 360

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, ht)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, wd)
cam.set(cv2.CAP_PROP_FPS, 23)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
eyeCascade= cv2.CascadeClassifier('haar/haarcascade_eye_tree_eyeglasses.xml')

while True:
    ignore, frame=cam.read()

    frameGray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray, 1.1, 5)
    # print(faces)
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        frameFaceGray=frameGray[y:y+h,x:x+w]
        eyes=eyeCascade.detectMultiScale(frameFaceGray, 1.1,5)
        for eye in eyes:
            xe, ye, we, he = eye
            cv2.rectangle(frame,(x+xe,y+ye),(x+xe+we,y+ye+he),(255,0,255),3)


    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    