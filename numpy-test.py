import numpy as np
# frame=np.array([[0,0,0],[0,0,0],[0,0,0]])
# print(frame)
# print('\n')

# # [row,column]
# frame[1,2] = 1 #indexing starts with 0

# frame1=np.zeros([5,5],dtype=np.uint8)
# print(frame1)

# # [range1:range2, col rang1:range2] where range2 is not inclusive
# frame1[0:2,0:5] =100
# print(frame1)

# frame[:,0:2]=255
# print(frame)

frameBGR = np.zeros([2,2,3],dtype=np.uint8)

#setting BGR value of pixel at (0,0) to (128,255,128)
frameBGR[0,0,0]=128
frameBGR[0,0,1]=255
frameBGR[0,0,2]=128

print(frameBGR)