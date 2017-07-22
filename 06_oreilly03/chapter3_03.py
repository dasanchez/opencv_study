import cv2
from sys import argv

""" Load and blend two images using alpha blending """

# Define Region of Interest (ROI)
alpha = float(argv[3])
beta = float(argv[4])
x = int(argv[5])
y = int(argv[6])

# Load background image
bgImg = cv2.imread(argv[1],1)

# Load foreground image
fgImg = cv2.imread(argv[2],1)

# Get ROI
height, width = fgImg.shape[:2]
roi = bgImg[y:y+height,x:x+width]
cv2.addWeighted(fgImg, alpha, roi, beta, 0, roi)

cv2.imshow("Alpha blending",bgImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

