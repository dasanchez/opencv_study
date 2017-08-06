import cv2
import numpy as np
import pprint
import sys
""" Use masks to lower the green level on a picture. """

"""
2 arguments:
    argv[1]: File name
    argv[2]: Green channel threshold, in percentage
    argv[3]: Adjustment
"""

thresh = 255*float(sys.argv[2])

img = cv2.imread(sys.argv[1],1)
cv2.namedWindow("Original image", cv2.WINDOW_NORMAL)
cv2.imshow("Original image",img)
b,g,r = cv2.split(img)

'''
Use threshold function:
    1st arg: source
    2nd arg: threshold value
    3rd arg: new value
    4th arg: flag
    If the pixel in source is greater than the threshold, it is assigned another value.
    The returned mask will have 0 for everything under the threshold, and 255 for everything greater or equal to.
'''
ret, g_mask = cv2.threshold(g,thresh, 255, cv2.THRESH_BINARY)
cv2.namedWindow("Mask",cv2.WINDOW_NORMAL)
cv2.imshow("Mask",g_mask)

masked = g.copy()
nonmasked = g.copy()
cv2.subtract(g,int(sys.argv[3]),masked,g_mask)
cv2.subtract(g,int(sys.argv[3]),nonmasked)

img_proc = cv2.merge((b,masked,r))
nm_proc = cv2.merge((b,nonmasked,r))
cv2.namedWindow("Processed image", cv2.WINDOW_NORMAL)
cv2.imshow("Processed image", img_proc)
cv2.namedWindow("Nonmasked result", cv2.WINDOW_NORMAL)
cv2.imshow("Nonmasked result", nm_proc)

cv2.waitKey(0)
cv2.destroyAllWindows()

