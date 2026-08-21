import os 
import cv2
import face_recognition as fr
import json
import numpy as np

print(cv2.__version__)



knownImageDir='/home/agush/mainWS/workspaces/paulMcWhorter-OpenCV/demoImages/known'
font = cv2.FONT_HERSHEY_SIMPLEX
knownEncodings={}

for root, dirs, files in os.walk(knownImageDir):
    for file in files:
        filePath = os.path.join(root,file)
        faceImage=fr.load_image_file(filePath)
        faceEncoding=fr.face_encodings(faceImage)[0]
        knownEncodings[file]=faceEncoding

# write
with open('encodings.json', 'w') as f:
    json.dump({k: v.tolist() for k, v in knownEncodings.items()}, f)

# # read
# with open('encodings.json') as f:
#     knownEncodings = {k: np.array(v) for k, v in json.load(f).items()}

print(knownEncodings) 