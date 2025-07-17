import cv2
import mediapipe
import os
import numpy as np
import time

class DataCollector:
    '''' This constructor initilize the starting variable like gesture name, saving directory path, max samples we can collect'''
    def __init__(self,gesture_name,save_dir,max_samples= 100):
        self.gesture_name = gesture_name
        self.save_dir = save_dir
        self.max_samples = max_samples
        self.sampleCount = 0
        self.hands = mediapipe.solutions.hands.Hands()
        self.mp_draw = mediapipe.solutions.drawing_utils

        os.makedirs(self.save_dir,exist_ok=True)

    def extract_landmarks(self ,hand_landmarks):
        '''' This function process and conver the collected landmarks and return the landmarks array containg lmx,lmy,lmz'''
        return np.array([[lm.x,lm.y,lm.z]for lm in hand_landmarks.landmark]).flatten()
    
    def collect(self):
        '''' This function collect the data from the webcam using opencv and collect the landmarks using mediapipe and send that data to the further functions'''
        cap = cv2.VideoCapture(0)
        print(f"Shown gesture is : {self.gesture_name}")
        print(f"s to save samples and q to quit ")

        saving = False

        while cap.isOpened() and self.sampleCount<self.max_samples:
            ret,frame = cap.read()
            if not ret:
                break

            img_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            results = self.hands.process(img_rgb)

            if results.multi_hand_landmarks:
                for hand_landmark in results.multi_hand_landmarks:
                  self.mp_draw.draw_landmarks(frame,hand_landmark,mediapipe.solutions.hands.HAND_CONNECTIONS)

                  if saving and self.sampleCount<self.max_samples:
                    landmarks = self.extract_landmarks(hand_landmark)
                    np.save(os.path.join(self.save_dir,f"{self.sampleCount}.npy"),landmarks)
                    self.sampleCount+=1
                    print(f"Sample {self.sampleCount} saved! ")
            cv2.putText(frame,f"gesture : {self.gesture_name} | Saved : {self.sampleCount}",(10,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow("DataCollector",frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                saving =True
                print("Saving")
            elif key == ord('a'):
                saving = False
        cap.release()
        cv2.destroyAllWindows()
        print(f"📦 Done collecting {self.sampleCount} samples for '{self.gesture_name}'")


