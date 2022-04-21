import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture(0) #Set 0 for webcam or adding a string with path to the video
pTime = 0

mpdraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpdraw.DrawingSpec(thickness=1, circle_radius=1)
while True:
    success, img = cap.read()
    imgRBG = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRBG)
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpdraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)
            for id, lm in enumerate(faceLms.landmark):
                ih, iw, ic = img.shape
                x, y = int(lm.x*iw), (lm.y*ih)
                print(id, x, y)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    flip = cv.flip(img, 1)
    cv.putText(img, f'FPS: {int(fps)}', (20, 70), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    cv.imshow("Image", flip)
    cv.waitKey(1)