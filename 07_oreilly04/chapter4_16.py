"""
Warp Perspective Program.
Open an image.
When the user presses a key between 1 and 9,
the corresponding cell in the transformation
matrix will be increased accordingly.
If the Shift key is pressed at the same time,
the cell value will decrease instead.
Show the raw and transformed images in separate windows.
"""

import sys
import numpy as np
import cv2

raw_title = 'Raw image'
dst_title = 'Transformed image'

cv2.namedWindow(raw_title)
cv2.namedWindow(dst_title)

# Display raw image
img = cv2.imread(sys.argv[1], 1)
cv2.imshow(raw_title, img)

rows, cols, ch = img.shape
print "image size: ", rows, "rows x ", cols, "cols"

# We can use the image size to set our perspective points - we need four.
pts1 = np.float32([[cols/4, rows/4], [3*cols/4, rows/4], [3*cols/4, 3*rows/4], [cols/4, 3*rows/4]])
pts2 = np.float32([[0, 0], [cols, 0], [cols, rows], [0, rows]])

# Get perspective transform
M = cv2.getPerspectiveTransform(pts1, pts2)
print M
dst = cv2.warpPerspective(img, M, (600, 400))
cv2.imshow(raw_title, img)
cv2.imshow(dst_title, dst)

while True:
    k = cv2.waitKey(10) & 0xFF
    if k is not 255:
        if k == ord('q'):
            break
        if k == ord('1'):
            M[0, 0] += 1
        elif k == ord('!'):
            if M[0, 0] >= 1:
                M[0, 0] -= 1
        elif k == ord('2'):
            M[0, 1] += 1
        elif k == ord('@'):
            if [M, 1] >= 1:
                M[0, 1] -= 1
        elif k == ord('3'):
            M[0, 2] += 1
        elif k == ord('#'):
            if M[0, 2] >= 1:
                M[0, 2] -= 1
        elif k == ord('4'):
            M[1, 0] += 1
        elif k == ord('$'):
            if M[1, 0] >= 1:
                M[1, 0] -= 1
        elif k == ord('5'):
            M[1, 1] += 1
        elif k == ord('%'):
            if M[1, 1] >= 1:
                M[1, 1] -= 1
        elif k == ord('6'):
            M[1, 2] += 1
        elif k == ord('^'):
            if M[1, 2] >= 1:
                M[1, 2] -= 1
        elif k == ord('7'):
            M[2, 0] += 1
        elif k == ord('&'):
            if M[2, 0] >= 1:
                M[2, 0] -= 1
        elif k == ord('8'):
            M[2, 1] += 1
        elif k == ord('*'):
            if M[2, 1] >= 1:
                M[2, 1] -= 1
        elif k == ord('9'):
            M[2, 2] += 1
        elif k == ord('('):
            if M[2, 2] >= 1:
                M[2, 2] -= 1
        print M
        dst = cv2.warpPerspective(img, M, (600, 400))
        cv2.imshow(dst_title, dst)
cv2.destroyAllWindows()
