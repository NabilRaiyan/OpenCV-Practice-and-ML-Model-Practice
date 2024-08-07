import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cat.jpeg')
cv.imshow('Cat', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 125)
cv.imshow("Canny", canny)


# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)


ret, thresh = cv.threshold(gray, 125, 255)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# print(f'This contours {len(contours)} found')

cv.waitKey(0)