
################### Simple Detect #############
# import cv2
# import numpy as np
#
# def MosueClick(event,x,y,flags,params):
#     if event==cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#
# img =cv2.imread("D:\Project\OpenCVTutorials\Resource\phone.jpg")
#
# cv2.imshow("original image",img)
# cv2.setMouseCallback("original image",MosueClick)
# cv2.waitKey(0)

######### WARP PRESPECTIVE IMPLEMANTAION WITH MOUSE CLICKS ##################

import cv2
import numpy as np


circles =np.zeros((4,2),np.int)
counters = 0

def MosueClick(event,x,y,flags,params):
    global counters
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[counters]=x,y
        counters =counters+1
        #print(circles)


img = cv2.imread('D:\Project\OpenCVTutorials\Resource\phone.jpg')

while True:
    if counters==4:
        width, height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Output Image ", imgOutput)

    for x in range (0,4):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),5,(0,255,0),cv2.FILLED)

    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ",MosueClick)

    cv2.waitKey(1)