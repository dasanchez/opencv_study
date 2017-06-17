import cv2
import filters
import time

rawImage = cv2.imread('bluejays.jpg',1)
filtImage = rawImage
cv2.imshow("Image", rawImage)
cv2.waitKey(0)

filters.recolorRC(rawImage,filtImage)
cv2.imshow("Image", filtImage)
cv2.waitKey(0)

filters.recolorRGV(rawImage,filtImage)
cv2.imshow("Image", filtImage)
cv2.waitKey(0)

filters.recolorCMV(rawImage,filtImage)
cv2.imshow("Image", filtImage)
cv2.waitKey(0)

cv2.destroyAllWindows()

