import cv2
import numpy as np

""" Draw a circle on a 100 x 100 matrix """
image = np.zeros((100,100,3),np.uint8)
cv2.circle(image, (50,50), 40, (0,255,0), 1, 8)

cv2.imshow("Circle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

