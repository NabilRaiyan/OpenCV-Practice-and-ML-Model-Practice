import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# # Paint the image a certain color
# blank[200:300, 300:400] = 200, 255, 150
# cv.imshow('Green', blank)

# Draw a rectangle
cv.rectangle(blank, (100, 100), (250, 500), (0, 255, 0), thickness=2)
cv.imshow('Rectangle', blank)


# Draw a circle
cv.circle(blank, (250, 250), 40, (100, 180, 20), thickness=-1)
cv.imshow('Circle', blank)

# Draw a line
cv.line(blank, (50, 50), (220, 220), (100, 180, 20), thickness = 3)
cv.imshow('Line', blank)

# Write text

cv.putText(blank, "Hello my name is Raiyan", (225, 80), cv.FONT_HERSHEY_TRIPLEX, fontScale = 1.0, color=(100, 200, 20), thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)