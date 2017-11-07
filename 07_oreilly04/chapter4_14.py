"""
Simple Paint Program.
Create a blank (zeroed) image.
Allow the user to draw rectangles, ellipses, circles, and polygons using the left mouse button.
Allow the user to "erase" using the right mouse button.
"""

import math
import sys
import numpy as np
import cv2

cur_colour = [255, 0, 0]
cur_shape = 0 # 0: rec, 1: cir, 2: ell, 3: pol
drawing = False
erasing = False
ix, iy = -1, -1
rec_width, rec_h = -1, -1
segment_w, segment_h = 0, 0
sin60 = math.sin(math.pi*60/180)

def b_changed(pos):
    """
    Update blue component
    """
    cur_colour[0] = pos
    colour_area[:, :] = cur_colour
    colour_area_bottom = shape_area.shape[0]+colour_area.shape[0]
    canvasImg[shape_area.shape[0]:colour_area_bottom, 0:colour_area.shape[1]] = colour_area
    cv2.imshow('OpenCV Paint', canvasImg)

def g_changed(pos):
    """
    Update green component
    """
    cur_colour[1] = pos
    colour_area[:, :] = cur_colour
    colour_area_bottom = shape_area.shape[0]+colour_area.shape[0]
    canvasImg[shape_area.shape[0]:colour_area_bottom, 0:colour_area.shape[1]] = colour_area
    cv2.imshow('OpenCV Paint', canvasImg)

def r_changed(pos):
    """
    Update Red component
    """
    cur_colour[2] = pos
    colour_area[:, :] = cur_colour
    colour_area_bottom = shape_area.shape[0]+colour_area.shape[0]
    canvasImg[shape_area.shape[0]:colour_area_bottom, 0:colour_area.shape[1]] = colour_area
    cv2.imshow('OpenCV Paint', canvasImg)

def highlight_shape(shape_index):
    """
    Highlight a shape in the shape area.
    """
    global canvasImg, segment_w, segment_h, rec_area, cir_area, ell_area, pol_area, shapes
    # Copy shape from original canvas
    #bare_shapes = shape_area.copy()
    shape_area = bare_shape_area.copy()
    # Set ROI depending on mouse coordinates
    highlight = shape_area[shapes[shape_index][0][1]:shapes[shape_index][1][1],\
     shapes[shape_index][0][0]:shapes[shape_index][1][0]]
    cv2.bitwise_not(highlight, highlight)
    #activeImg = canvasImg.copy()
    #activeImg[0:shape_area.shape[0], 0:shape_area.shape[1]] = shape_area
    canvasImg[0:shape_area.shape[0], 0:shape_area.shape[1]] = shape_area
    cv2.imshow('OpenCV Paint', canvasImg)

def highlight_region(x):
    """
    Select a shape given the x coordinate of the mouse click.
    """
    global segment_w, cur_shape
    # Highlight one of the shapes
    # x given to decide where to fall in.
    if x < segment_w:
        cur_shape = 0
        highlight_shape(0)
    elif x < segment_w*2:
        cur_shape = 1
        highlight_shape(1)
    elif x < segment_w*3:
        cur_shape = 2
        highlight_shape(2)
    elif x < segment_w*4:
        cur_shape = 3
        highlight_shape(3)

def hexagonPoints(p1x, p1y, y_offset):
    """
    Return array of vertices using the inputs as centre and corner coordinates.
    """
    # First vertex is the same as P1 (P0 being the centre point)
    radius = math.sqrt((ix-p1x)*(ix-p1x)+(iy-y_offset-p1y)*(iy-y_offset-p1y))

    v0x = ix + radius
    v0y = iy - y_offset

    v1x = ix + (radius / 2)
    v1y = iy - y_offset + radius * sin60

    v2x = ix - (radius / 2)
    v2y = v1y

    v3x = ix - radius
    v3y = iy - y_offset

    v4x = v2x
    v4y = iy - y_offset - radius * sin60

    v5x = v1x
    v5y = v4y

    pts = np.array([[v0x, v0y], [v1x, v1y], [v2x, v2y], [v3x, v3y], [v4x, v4y], [v5x, v5y]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    return pts

def mouseEvent(event, x, y, flags, param):
    """
    Handle mouse events.
    """
    global totalh, w, h, drawing, erasing, ix, iy, rec_w, rec_h,\
     segment_h, cur_shape, shape_area, colour_area, drawing_area
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > segment_h:
            drawing = True
            ix, iy = x, y
    elif event == cv2.EVENT_RBUTTONDOWN:
        if y > (segment_h+2):
            drawing = False
            erasing = True
            # Erase a 5x5 area
            cv2.circle(canvasImg, (x,y), 5, (0, 0, 0), -1)
            cv2.imshow('OpenCV Paint', canvasImg)
    elif event == cv2.EVENT_RBUTTONUP:
        erasing = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing and y > segment_h:
            if cur_shape == 0: # Rectangle
                rec_w = x-ix
                rec_h = y-iy
                #drawImg = drawing_area.copy()
                drawImg = canvasImg.copy()
                cv2.rectangle(drawImg, (ix, iy), (x, y), (250, 250, 250), 1)
                canvasTemp = canvasImg.copy()
                #canvasTemp = canvasTemp[(canvasImg.shape[1]*2/10):canvasImg.shape[1]-1,\
                #0:canvasImg.shape[0]]
                cv2.imshow('OpenCV Paint', drawImg)
            elif cur_shape == 1: # Circle
                cir_rad = math.sqrt((ix-x)*(ix-x)+(iy-y)*(iy-y))
                drawImg = canvasImg.copy()
                cv2.circle(drawImg, (ix, iy), int(cir_rad), (250, 250, 250), 1)
                cv2.imshow('OpenCV Paint', drawImg)
            elif cur_shape == 2: # Ellipse
                ell_centre = (ix, iy)
                ell_axes = (abs(x - ix), abs(y - iy))
                drawImg = canvasImg.copy()
                cv2.ellipse(drawImg, ell_centre, ell_axes, 0, 0, 360, (250, 250, 250), 1)
                cv2.imshow('OpenCV Paint', drawImg)
            elif cur_shape == 3: # Pentagon
                # The polygon will be defined by the user using a circumscribed circle.
                # The centre is already given, but the distance from it will dictate
                # the position of the next point.
                drawImg = canvasImg.copy()
                pol_arr = hexagonPoints(x, y, 0)
                cv2.polylines(drawImg, [pol_arr], True, (250, 250, 250))
                cv2.imshow('OpenCV Paint', drawImg)
        elif erasing is True and y > (segment_h+2):
            cv2.circle(canvasImg, (x,y), 5, (0, 0, 0), -1)
            cv2.imshow('OpenCV Paint', canvasImg)
    elif event == cv2.EVENT_LBUTTONUP:
        # Check if button landed on a "hot" region.
        # Shapes:
        if y < segment_h:
            highlight_region(x)
        else:
            # drawing area
            if drawing and y > segment_h:
                if cur_shape == 0:
                    rec_w = x - ix
                    rec_h = y - iy
                    if math.fabs(rec_w) > 0 and math.fabs(rec_h) > 0:
                        cv2.rectangle(canvasImg, (ix, iy), (x, y), cur_colour, -1)
                        cv2.imshow('OpenCV Paint', canvasImg)
                elif cur_shape == 1:
                    # Circle
                    # Because we are drawing using the radius, we might overlap with upper sections.
                    # We need to copy the canvas first, draw on that, and then add it back to the window.
                    cir_rad = math.sqrt((ix-x)*(ix-x)+(iy-y)*(iy-y))
                    tempDrawing = canvasImg.copy()
                    tempDrawing = tempDrawing[90:canvasImg.shape[0]-1,\
                    0:canvasImg.shape[1]]
                    cv2.circle(tempDrawing, (ix,iy-90), int(cir_rad), cur_colour, -1)
                    canvasImg[90:canvasImg.shape[0]-1, 0:canvasImg.shape[1]] = tempDrawing
                    cv2.imshow('OpenCV Paint', canvasImg)
                elif cur_shape == 2:
                    # Ellipse
                    # Because we are drawing using the axes, we might overlap with upper sections.
                    # We need to copy the canvas first, draw on that, and then add it back to the window.
                    ell_centre = (ix, iy-90)
                    ell_axes = (abs(x - ix), abs(y - iy))
                    tempDrawing = canvasImg.copy()
                    tempDrawing = tempDrawing[90:canvasImg.shape[0]-1,\
                    0:canvasImg.shape[1]]
                    cv2.ellipse(tempDrawing, ell_centre, ell_axes, 0, 0, 360, cur_colour, -1)
                    canvasImg[90:canvasImg.shape[0]-1, 0:canvasImg.shape[1]] = tempDrawing
                    cv2.imshow('OpenCV Paint', canvasImg)
                elif cur_shape == 3:
                    # Hexagon
                    tempDrawing = canvasImg.copy()
                    tempDrawing = tempDrawing[90:canvasImg.shape[0]-1,\
                    0:canvasImg.shape[1]]
                    pol_arr = hexagonPoints(x, y-90, 90)
                    cv2.polylines(tempDrawing, [pol_arr], True, (250, 250, 250))
                    cv2.fillPoly(tempDrawing, [pol_arr], cur_colour, 1)
                    canvasImg[90:canvasImg.shape[0]-1, 0:canvasImg.shape[1]] = tempDrawing
                    cv2.imshow('OpenCV Paint', canvasImg)
            drawing = False

cv2.namedWindow('OpenCV Paint')
canvasImg = np.zeros((800, 600, 3), np.uint8)

# The canvas needs to be split into three regions: shapes, colour, and drawing area.
shape_area = np.zeros((60, 600, 3), np.uint8)
colour_area = np.zeros((30, 600, 3), np.uint8)
drawing_area = np.zeros((620, 600, 3), np.uint8)

# Draw Shape Selectors
# Divide width over 4 equal segments for rectangle, circle, ellpise, and polygon.

segment_w = shape_area.shape[1]/4
segment_h = shape_area.shape[0]

rec_area = [(0, 0), (segment_w-1, segment_h-1)]
cir_area = [(segment_w, 0), (2*segment_w-1, segment_h-1)]
ell_area = [(2*segment_w, 0), (3*segment_w-1, segment_h-1)]
pol_area = [(3*segment_w, 0), (4*segment_w-1, segment_h-1)]

shapes = [rec_area, cir_area, ell_area, pol_area]

# Rectangle
# 1st corner, 2nd corner, colour, thickness
cv2.rectangle(shape_area, (segment_w/2-segment_w/4, segment_h/2-segment_h/4),\
(segment_w/2+segment_w/4, segment_h/2+segment_h/4), (250, 250, 250), 2)

# Circle
# Centre, radius, colour, thickness
cv2.circle(shape_area, (segment_w*3/2, segment_h/2), segment_h/4, (250, 250, 250), 2, 4)

# Ellipse
# Centre, major axis length, minor axis length, rotation, start angle, end angle, colour, thickness
cv2.ellipse(shape_area, (segment_w*5/2, segment_h/2), (segment_w/5, segment_h/4),\
30, 0, 360, (250, 250, 250), 2)

# Polygon
# Five points, open/closed, colour, thickness
polypoints = np.array([[(segment_w*7/2, segment_h/4), (segment_w*7/2+segment_w/6, segment_h*7/16),\
(segment_w*7/2+segment_w/11, segment_h*4/5), (segment_w*7/2-segment_w/10, segment_h*4/5),\
(segment_w*7/2-segment_w/6, segment_h*7/16)]], np.int32)
polypoints = polypoints.reshape((-1, 1, 2))
cv2.polylines(shape_area, [polypoints], True, (255, 255, 255), 2)

bare_shape_area = shape_area.copy()

'''
    Paint strip with cur_colour
'''

colour_area[:, :] = [255, 0, 0]

canvasImg = np.concatenate((shape_area, colour_area), axis=0)
canvasImg = np.concatenate((canvasImg, drawing_area), axis=0)

#colour_area = canvasImg[(canvasImg.shape[1]/10):(canvasImg.shape[1]*3/20)-1, 0:canvasImg.shape[0]-1]

cv2.setMouseCallback('OpenCV Paint', mouseEvent)
cv2.createTrackbar('B', 'OpenCV Paint', 255, 255, b_changed)
cv2.createTrackbar('G', 'OpenCV Paint', 0, 255, g_changed)
cv2.createTrackbar('R', 'OpenCV Paint', 0, 255, r_changed)
cv2.imshow('OpenCV Paint', canvasImg)
highlight_shape(0)

while cv2.waitKey(10) & 0xFF != ord('q'):
    pass
cv2.destroyAllWindows()
