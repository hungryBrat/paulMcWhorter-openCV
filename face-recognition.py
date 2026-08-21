import cv2
import face_recognition as fr
font = cv2.FONT_HERSHEY_SIMPLEX

donFace=fr.load_image_file('/home/agush/mainWS/workspaces/paulMcWhorter-OpenCV/demoImages/known/Donald Trump.jpg')

# face location returns array of array where each array is [top, right, bottom, left ] of each face
faceLoc=fr.face_locations(donFace)[0]
# top, right, bottom, left = faceLoc
# print(faceLoc)

# returns an array of arrays, but we know theres only 1 face
donFaceEncoding=fr.face_encodings(donFace)[0]



nancyFace=fr.load_image_file('demoImages/known/Nancy Pelosi.jpg')

# face location returns array of array where each array is [top, right, bottom, left] of each face
nancyFaceLoc=fr.face_locations(nancyFace)[0]
# top, right, bottom, left = faceLoc
# print(nancyFaceLoc)

# returns an array of arrays, but we know theres only 1 face
nancyFaceEncoding=fr.face_encodings(nancyFace)[0]

# book keeping of known faces
knownEncodings={'Donald Trump' : donFaceEncoding, 'Nancy Pelosi' : nancyFaceEncoding}


# taking an unknown image and book keeping encodings of evry unknown face
unknownFace=fr.load_image_file('demoImages/unknown/u11.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
unknownFaceLocations=fr.face_locations(unknownFace)
unknownFaceEncodings=fr.face_encodings(unknownFace,unknownFaceLocations)

for location, encoding in zip(unknownFaceLocations, unknownFaceEncodings):
    name='Unidentified'
    top, right, bottom, left= location
    cv2.rectangle(unknownFaceBGR, (left,top), (right,bottom), (255,255,255), 3) 
    matches = fr.compare_faces(list(knownEncodings.values()), encoding)
    # print(matches)
    for matched, named in zip(matches, knownEncodings.keys()):
        if matched:
            name = named
            break
    cv2.putText(unknownFaceBGR, name, (left,top-10),font, 0.5, (0,0,255),2) 

cv2.imshow('myWin', unknownFaceBGR)
cv2.waitKey(5000)

# # face-recognition works in RGB but cv2 works in BGR so need to color convert to correctly display the file
# donFaceBGR=cv2.cvtColor(donFace, cv2.COLOR_RGB2BGR)
# cv2.rectangle(donFaceBGR, (left,top), (right,bottom), (255,255,255), 3)
# cv2.imshow('myWin', donFaceBGR)
# cv2.waitKey(5000)