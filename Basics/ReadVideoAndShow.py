import cv2

capture = cv2.VideoCapture("D:\Project\OpenCVTutorials\Resource\dog.mp4")
framewith =320
framhight=240
capture.set(3,framhight)
capture.set(4,framhight)
while True:
    sueccess , frame = capture.read()

    frame =cv2.resize(frame,(framewith,framhight))

    cv2.imshow("frame ",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    