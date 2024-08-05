# Ctrl + Alt + M to stop python file exe

import cv2 as cv

# reading image from pc
img = cv.imread('Photos/img-1.png')
cv.imshow('Cat', img)

cv.waitKey(0)


# # reading video from pc

# capture = cv.VideoCapture('Videos/video-1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()

# cv.destroyAllWindows()


