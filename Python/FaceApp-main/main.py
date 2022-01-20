from cv2 import cv2 as cv
import cvzone as cvz
vid = cv.VideoCapture(0)
cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
overlay = cv.imread('sunglass.png', -1)
while True:
    _, frame = vid.read()
    gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray_scale)
    for(x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        overlay_resize = cv.resize(overlay, (w, h))
        frame = cvz.overlayPNG(frame, overlay_resize, [x, y])
    cv.imshow('Test', frame)
    if cv.waitKey(1) == ord('a'):
        break