import cv2
import imutils
img = cv2.imread("sample1.jpg")
resizedImg = imutils.resize(img,width=20)
cv2.imwrite("resizedImage.jpg",resizedImg)
