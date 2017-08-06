import cv2
import numpy as np

""" Use ROI to draw a pyramid of radially increasing values in grayscale. """
square_side = 210
border_width = 10
color = 0

img = np.zeros((square_side,square_side,1),np.uint8)
region_side = square_side
widths = 0

while region_side >= border_width:
    region = img[widths*border_width:(widths*border_width)+region_side,widths*border_width:(widths*border_width)+region_side]
    region[:] = color
    color += 20
    region_side -= 2*border_width
    widths += 1

cv2.imshow("Pyramid", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

