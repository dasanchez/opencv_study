import cv2
import numpy as np

""" Draw a diagonal red line """
image = np.zeros((512,512,3),np.uint8)
cv2.line(image, (20,20), (100,75), (0,0,255), 5, 10)
cv2.rectangle(image, (120, 20), (200,95), (255,0,0), 3)
cv2.circle(image, (275,50), 45, (0,255,0), 4, 4)
cv2.ellipse(image, (425, 50), (60, 20), 10, 0, 270,(0,255,255),-1)

pts = np.array([[10,125],[80,150],[52,205]], np.int32)
pts = pts.reshape((-1,1,2))
fpts = np.array([[130,125],[210,150],[182,205]], np.int32)
fpts = fpts.reshape((-1,1,2))
cv2.polylines(image, [pts],True,(255,0,0))
cv2.fillPoly(image, [fpts],(0,255,0))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'OpenCV Text', (250, 175), font, 2, (0,255,255),4, cv2.LINE_AA)

cv2.imshow("Shapes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

