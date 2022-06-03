import cv2
import numpy as np
from pyzbar.pyzbar import decode

#img= cv2.imread("1.png")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open("myDataFile.text") as f:
    myDatalist = f.read().splitlines()
print(myDatalist)

while True:
    suecuss , img =cap.read()
    for barcode in decode(img):
        mydata=barcode.data.decode('utf-8')
        print(mydata)
        if mydata in myDatalist:
            output = "autorized"
            mycolor=(0,0,255)
        else:
            output = "unautorized"
            mycolor = (255, 0, 0)
        pts=np.array([barcode.polygon],np.int32)
        pts=pts.reshape(-1,1,2)
        cv2.polylines(img,[pts],True,mycolor,5)
        pts2=barcode.rect
        cv2.putText(img,output,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_PLAIN,0.9,mycolor,3)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
