import os 
import cv2
import face_recognition as fr
print(cv2.__version__)

imageDir='/home/agush/mainWS/workspaces/paulMcWhorter-OpenCV/demoImages'

for root, dirs, files in os.walk(imageDir):
    print('roots: ', root)
    print('dirs: ', dirs)
    print('files: ', files)
    for file in files:
        print(os.path.join(root,file)) # full path of that file from root 
        name=os.path.splitext(file)
        print(name)