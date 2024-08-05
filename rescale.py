import cv2 as cv

# reading image from pc
img = cv.imread('Photos/img-3.png')
# cv.imshow('Cat', img)


# change resulation of a video

# method for Live Video
def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)



# rescaling function 
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# resized_img = rescaleFrame(img)
# cv.imshow('Resized Image', resized_img)
# cv.waitKey(0)

capture = cv.VideoCapture('Videos/video-1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

# cv.destroyAllWindows()