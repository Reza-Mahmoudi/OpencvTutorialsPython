import cv2
import numpy as np

img =np.zeros((512,512,3),np.uint8)
print(img)

#img[:]=0,0,255

#draw line
cv2.line(img,(15,15),(300,200),(255,0,0),5,3)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),5,2)

#shape regtangel

cv2.rectangle(img,(350,100),(450,200),(255,0,0),3,2)
cv2.rectangle(img,(300,200),(110,220),(0,255,0),cv2.FILLED)

#shape circle

cv2.circle(img,(250,250),15,(255,250,0),3)
#circle Filed
cv2.circle(img,(250,100),15,(100,250,0),cv2.FILLED)
#warp puttex
cv2.putText(img,"Hello OPencv",(100,160),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)


cv2.imshow("image",img)
cv2.waitKey(0)