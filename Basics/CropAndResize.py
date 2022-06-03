import  cv2

img = cv2.imread("D:\Project\OpenCVTutorials\Resource\lena.png")

cv2.imshow("image",img)

print(img.shape)

framewitdh ,framehight=640,480

#image resize
imageResize =cv2.resize(img,(framewitdh,framehight))

cv2.imshow('Resize ',imageResize)
#shape
print(imageResize.shape)

#crop by point
croped = img[200:480]
cv2.imshow("croped ",croped)
#croped by points
crope2point =img[200:350,200:550]

cv2.imshow('crope2point ',crope2point)


#image resize after crop

#image resize
imageCropResize =cv2.resize(croped,(img.shape[0],img.shape[1]))

cv2.imshow('imageCropResize ',imageCropResize)


#image resize
imageCrop2pointResize =cv2.resize(crope2point,(img.shape[0],img.shape[1]))

cv2.imshow('imageCrop2pointResize ',imageCrop2pointResize)

cv2.waitKey(0)