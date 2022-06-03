import cv2

# LOAD AN IMAGE USING 'IMREAD'

img = cv2.imread("D:\Project\OpenCVTutorials\Resource\lena.png")

# DISPLAY

cv2.imshow("image",img)

cv2.waitKey(0)

cv2.destroyAllWindows()

