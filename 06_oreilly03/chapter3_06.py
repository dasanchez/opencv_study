import cv2
import numpy as np

""" Draw a green rectangle on a 100 x 100 matrix """
b = np.zeros((100,100,1),np.uint8)
g = np.zeros((100,100,1),np.uint8)
r = np.zeros((100,100,1),np.uint8)
cv2.rectangle(g, (20,5), (40,20), 255, 1)

image = cv2.merge((b,g,r))

cv2.imshow("Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

