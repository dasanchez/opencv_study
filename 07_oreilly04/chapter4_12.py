import cv2
import numpy as np
import math
import sys

""" 
Open an image file and display it.
When the user drags over a rectangular region in the image, the region is highlighted.
The BGR histogram for the selected region is displayed on a separate window.
Arguments:
    0: filename
"""
dragging = False
ix, iy = -1,-1
width, height = -1,-1

def calcChannelHistogram(channel):
    hist = [0,0,0,0,0,0,0,0]
    for val in np.nditer(channel):
        if val < 32:
            hist[0] += 1
        if val >= 32 and val < 64:
            hist[1] += 1
        if val >= 64 and val < 96:
            hist[2] += 1
        if val >= 96 and val < 128:
            hist[3] += 1
        if val >=128 and val < 160:
            hist[4] += 1
        if val >=160 and val < 192:
            hist[5] += 1
        if val >=192 and val < 224:
            hist[6] += 1
        if val >=224:
            hist[7] += 1
    maxVal = max(hist)
    return maxVal,hist

def calcHistogram(region):
    global histImg, font, y_step, x_step, fontsize, fontwidth, lineColor
    # Split array in three channels:
    b,g,r  = cv2.split(region)
    b_max, b_hist = calcChannelHistogram(b)
    g_max, g_hist = calcChannelHistogram(g)
    r_max, r_hist = calcChannelHistogram(r)
    maxVals = [b_max,g_max,r_max]
    hists = [b_hist, g_hist, r_hist]
    # Copy template
    histDraw = histImg.copy()
    y_start_label = 15
    y_start_bars = 120
    for counter in range(3):
        # Normalize pixel counts
        if maxVals[counter]>100:
            normalize_ratio = (maxVals[counter]/100)+1
        else:
            normalize_ratio = 1
        # Max count
        cv2.putText(histDraw,str(maxVals[counter]),(2,y_start_label),font,0.5,lineColor[counter],1,cv2.LINE_8)
        y_start_label += y_step
        # X-Axis
        x_start = 56
        for val in hists[counter]:
            if val/normalize_ratio == 0:
                height = 1
            else:
                height = val/normalize_ratio
            cv2.rectangle(histDraw,(x_start-x_step/2,y_start_bars),(x_start+x_step/2,y_start_bars-height),lineColor[counter],-1)
            x_start += x_step
        y_start_bars += y_step
    
    cv2.imshow("Histogram",histDraw)

def mouseEvent(event, x, y, flags, param):
    global image,totalh,w,h,dragging, ix, iy, width, height
    if event == cv2.EVENT_LBUTTONDOWN:
        dragging = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dragging==True:
            width = x-ix
            height = y-iy
            drawImg = img.copy()
            cv2.rectangle(drawImg, (ix,iy),(x,y),(250,250,250),1)
            cv2.imshow('Highlight',drawImg)
    elif event == cv2.EVENT_LBUTTONUP:
        dragging = False
        drawImg = img.copy()
        cv2.rectangle(drawImg,(ix,iy),(ix+width,iy+height),(250,250,250),1)
        cv2.imshow('Highlight', drawImg)
        # Capture region for histogram
        if width <0 and height >0:
            histRegion = img[iy:iy+height,ix+width:ix]
        elif width <0 and height <0:
            histRegion = img[iy+height:iy,ix+width:ix]
        elif width >0 and height < 0:
            histRegion = img[iy+height:iy,ix:ix+width]
        else:
            histRegion = img[iy:iy+height,ix:ix+width]
        calcHistogram(histRegion)

cv2.namedWindow('Highlight')
cv2.namedWindow('Histogram')
font = cv2.FONT_HERSHEY_SIMPLEX
histImg = np.zeros((600,340,3),np.uint8)
img = cv2.imread(sys.argv[1])
cv2.setMouseCallback('Highlight', mouseEvent)
cv2.imshow('Highlight',img)
# Draw histogram labels
bar_labels = ['32','64','96','128','160','192','224','256']
fontsize = 0.5
fontwidth = 1
y_start = 160
y_step = 200
lineColor = [(250,100,100),(100,250,100),(100,100,250)]
for counter in range(3):
    x_start = 56
    x_step = 36
    for label in bar_labels:
        # Draw template
        cv2.putText(histImg,label,(x_start,y_start),font, fontsize, lineColor[counter], fontwidth, cv2.LINE_8)
        x_start += x_step
    y_start += y_step
cv2.imshow('Histogram',histImg)
while (cv2.waitKey(0) & 0xFF != ord('q')):
    pass
cv2.destroyAllWindows()

