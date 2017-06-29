import cv2

""" Load and display an image and a blurred version of it in two separate windows. """

cv2.namedWindow("Input")
cv2.namedWindow("Output")
img = cv2.imread('bluejays.jpg',1)
cv2.imshow("Input",img)
iplImg = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow("Output",iplImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

