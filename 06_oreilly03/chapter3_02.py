import cv2

""" Load and display an image file, and increase all the pixels in a Region of Interest. """

# Define Region of Interest (ROI)
x = 10
y = 10
width = 200
height = 100
# Value increase
px = 25 

# Load and modify image in grayscale
img = cv2.imread('bluejays.jpg',0)
cv2.imshow("Original Image Grayscale",img)

roiImg = img.copy()
roi = roiImg[y:y+height,x:x+width] # Define ROI using y and x as rows and cols, respectively
cv2.add(roi,px,roi)
roiImg[y:y+height,x:x+width]=roi
cv2.imshow("ROI Image Grayscale",roiImg)
print "Shape:" , roi.shape, "Gray original:", img[y,x], "Gray ROI:", roiImg[y,x]

# Load and modify image in BGR
colorImg = cv2.imread('bluejays.jpg',1)
cv2.imshow("Original Image Color", colorImg)

roiColorImg = colorImg.copy()
roiColor = colorImg[y:y+height, x:x+width]
b,g,r = cv2.split(roiColor) # ROI needs to be split up in channels because the cv2.add function only adds the first channel.
cv2.add(b,px,b)
cv2.add(g,px,g)
cv2.add(r,px,r)
roiColor = cv2.merge((b,g,r))
roiColorImg[y:y+height, x:x+width] = roiColor
cv2.imshow("ROI Image Color, BGR", roiColorImg)
print "Shape:", roiColor.shape, "Color original:", colorImg[y,x], "Color ROI:", roiColorImg[y,x]

roiHSVImg = cv2.cvtColor(colorImg, cv2.COLOR_BGR2HSV)
hsvImg = roiHSVImg.copy()
roiHSV = roiHSVImg[y:y+height, x:x+width]
h,s,v = cv2.split(roiHSV)
cv2.add(h,px,h)
cv2.add(s,px,s)
cv2.add(v,px,v)
roiHSV = cv2.merge((h,s,v,))
roiHSVImg[y:y+height,x:x+width] = roiHSV
hsv2bgrImg = cv2.cvtColor(roiHSVImg, cv2.COLOR_HSV2BGR)
cv2.imshow("ROI Image HSV, HSV", hsv2bgrImg)
print "Shape:", roiColor.shape, "HSV original:", hsvImg[y,x], "HSV ROI:", roiHSVImg[y,x]

cv2.waitKey(0)
cv2.destroyAllWindows()

