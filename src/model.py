import cv2 as cv
import mediapipe
import time
from hand_landmarks import HandDetector
from gestures import HandGestures

cap  = cv.VideoCapture(0)
previous_time = 0
current_time = 0
detector = HandDetector()
gestures = HandGestures()

while True:
    success,img = cap.read()
    img = detector.findHands(img)
    current_time= time.time()

    lmlist = detector.findPosition(img)

    fps=1/(current_time-previous_time)
    previous_time = current_time

        # if len(lmlist)!=0:
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    # getFingersUP(lmlist)
    for func in gestures.gesture_Functions:
        gesture  = func(img,lmlist)
        if gesture:
            cv.putText(img,gesture,(20,100),cv.FONT_HERSHEY_PLAIN,2,(255,0,255),2)



    cv.imshow("image",img)  

    # getFingersUP(lmlist)
    cv.waitKey(1)

