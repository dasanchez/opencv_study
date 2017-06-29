import cv2

""" Load and display an image and an version of it with edges detected in two separate windows. """

cv2.namedWindow("Input",cv2.WINDOW_NORMAL)
cv2.namedWindow("Output",cv2.WINDOW_NORMAL)
img = cv2.imread('bluejays.jpg',1)
cv2.imshow("Input",img)
edges = cv2.Canny(img,100,200)
cv2.imshow("Output",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

