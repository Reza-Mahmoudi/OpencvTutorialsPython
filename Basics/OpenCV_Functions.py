import cv2
import numpy as np

pth="D:\Project\OpenCVTutorials\Resource\lena.png"
img =cv2.imread(pth)
#convert BGR to Gray
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Filter gussian

gussianBlur = cv2.GaussianBlur(img,(3,3),3)

#Canny

thershold1=125
thershold2=175
canny = cv2.Canny(gussianBlur,thershold2,None)

#dilate

kernel = np.zeros((5,5),np.uint8)
dilated =cv2.dilate(canny,kernel,iterations =10)

#Erode image

eroded =cv2.erode(canny,kernel,iterations=2)

cv2.imshow("image",img)
cv2.imshow("Gray",gray)
cv2.imshow("Gaussian blur",gussianBlur)
cv2.imshow("canny ",canny)
cv2.imshow("dilate ",dilated)
cv2.imshow("erode ",eroded)
cv2.waitKey(0)
