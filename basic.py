import cv2 as cv
import numpy as np

img = cv.imread('Photos/Cat.jpeg')
cv.imshow('Cat', img)


# convert and image to gray scale
grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Scale', grayImg)

# Blur
blurImg = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow("Blured image", blurImg)


# Edge cascade



cv.waitKey(0)