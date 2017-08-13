import cv2

""" Load and display an image file. """


#img = cv2.imread('montreal.jpg',cv2.IMREAD_COLOR)
img = cv2.imread('montreal.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

