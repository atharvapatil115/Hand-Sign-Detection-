import numpy as np
import cv2 as cv 
import  mediapipe 
import time

class HandDetector():
    def __init__(self,mode =False,maxHands = 2,DetectCon = 0.5,trackCon = 0.5):
        
        self.mode = mode
        self.maxHands = maxHands
        self.DetectCon = DetectCon
        self.trackCon = trackCon

        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpdraw = mediapipe.solutions.drawing_utils

    def findHands(self,img):   
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                  for id,lm in enumerate(handlms.landmark):
                    height, width, channel = img.shape
                    cx,cy = int(lm.x*width) , int(lm.y*height)
                    # print(id,cx,cy)
                    # if id == 8:
                    cv.circle(img,(cx,cy),10,(255,0,255),cv.FILLED)
                    self.mpdraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)
                    self.mpdraw.draw_landmarks(img,handlms)
                    self.mpdraw.draw_landmarks(img,handlms,self.mpHands.HAND_CONNECTIONS)
        return img
    def findPosition(self,img,handNo = 0 , draw = True):
        lmlist = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            height,width,channel = img.shape
            for id,lm in enumerate(myHand.landmark):
                cx,cy = int(lm.x*width),int(lm.y*height)
                lmlist.append([id,cx,cy])
                if draw:
                    cv.circle(img,(cx,cy),2,(0,255,0),cv.FILLED)
        return lmlist


def main():
    
    cap  = cv.VideoCapture(0)
    previous_time = 0
    current_time = 0
    detector = HandDetector()
    while True:
        success,img = cap.read()
        img = detector.findHands(img)

      
        
                # print(results.multi_hand_landmarks) 
                

        current_time= time.time()
        lmlist = detector.findPosition(img)
        fps=1/(current_time-previous_time)
        previous_time = current_time
           


        # if len(lmlist)!=0:
        cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv.imshow("image",img)
        cv.waitKey(1)

if __name__=="__main__":
    main()