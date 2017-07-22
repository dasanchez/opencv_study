import cv2

""" Load and display an image file with a white rectangle drawn on top. """

color = (255,255,0)
thickness = 3

cv2.namedWindow("Image and Rectangle")
img = cv2.imread('bluejays.jpg',1)
cv2.rectangle(img, (5,5), (50,50), color, thickness)

cv2.imshow("Image and Rectangle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

