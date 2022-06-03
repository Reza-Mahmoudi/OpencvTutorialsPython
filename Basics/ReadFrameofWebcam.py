import cv2


framewith = 320 #640
framehight=240  #480

capture = cv2.VideoCapture(0) #or 0 / 1

capture.set(3,framewith)
capture.set(4,framehight)

while True:
    suessues ,frame = capture.read()

    cv2.imshow("Result",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


