import cv2
print(cv2.__version__)

wd= 640
ht= 360

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, ht)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, wd)
cam.set(cv2.CAP_PROP_FPS, 23)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame=cam.read()
    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    