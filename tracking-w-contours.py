import cv2
import numpy as np
print(cv2.__version__)

def onTrack1(val):
    global hueLow
    hueLow=val

def onTrack3(val):
    global satLow
    satLow=val

def onTrack5(val):
    global valLow
    valLow=val

def onTrack2(val):
    global hueHigh
    hueHigh=val

def onTrack4(val):
    global satHigh
    satHigh=val

def onTrack6(val):
    global valHigh
    valHigh=val


wd= 640
ht= 360

hueHigh=20
hueLow=10
satHigh=150
satLow=10
valHigh=150
valLow=10

cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, ht)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, wd)
cam.set(cv2.CAP_PROP_FPS, 23)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('HSV Trackers')
cv2.moveWindow('HSV Trackers', wd, 0)

cv2.createTrackbar('Hue Low', 'HSV Trackers', 10, 179,onTrack1)
cv2.createTrackbar('Hue High', 'HSV Trackers', 20, 179,onTrack2)
cv2.createTrackbar('Sat Low', 'HSV Trackers', 10, 255,onTrack3)
cv2.createTrackbar('Sat High', 'HSV Trackers', 150, 255,onTrack4)
cv2.createTrackbar('Val Low', 'HSV Trackers', 10, 255,onTrack5)
cv2.createTrackbar('Val High', 'HSV Trackers', 150, 255,onTrack6)

while True:
    ignore, frame=cam.read()

    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    mask=cv2.inRange(frameHSV, lowerBound,upperBound) # creates a mask of same shape as frameHSV and keeps only in rAnge pixels as white
    # cv2.imshow('My Mask',mask)

    #creating a smaller mask for display
    maskSmall=cv2.resize(mask,(int(wd/2),int(ht/2)))
    cv2.imshow('My Mask',maskSmall)
    cv2.moveWindow('My Mask', 0,int(ht*3/2))

    #creating masked out Object frame
    # maskObj=cv2.bitwise_and(frame,frame, mask=mask)
    # maskObjSmall=cv2.resize(maskObj, (int(wd/2),int(ht/2)))
    # cv2.imshow('My Object',maskObjSmall)
    # cv2.moveWindow('My Object', wd,int(ht*3/2))

    #creaing contours -- gotta work with the original mask
    #a contour is aN Array of arrays where each inner array is a series of continous contour points

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.drawContours(frame,contours, -1, (255,0,0), 3)
    # can draw the contours directly but small ones make noise

    for contour in contours:
        area=cv2.contourArea(contour)
        if area>=100:
            # cv2.drawContours(frame,[contour], 0, (255,0,0), 3)
            x,y,w,h=cv2.boundingRect(contour) #takes one array of contours and returns the four corners of the box
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)


    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
    