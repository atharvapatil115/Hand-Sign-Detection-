import cv2 as cv

class HandGestures():
    
    def  __init__(self):
        self.gesture_Functions = [  self.isILoveYou,
                                    self.IsPeace,
                                    self.IsAbuse,
                                    self.IsHello,
                                    self.IsStop]

    def isILoveYou(self,img,lmlist):
        if len(lmlist) == 0:
         return
        if (lmlist[12][2]>lmlist[11][2] and 
            lmlist[8][2]<lmlist[7][2]   and 
            lmlist[16][2]>lmlist[15][2] and 
            lmlist[20][2]<lmlist[19][2] and 
            lmlist[4][1]>lmlist[3][1]):
            
            return "I Love You <3"
        return None
    
    def IsPeace(self,img,lmlist):
        if (len(lmlist) == 0):
            return
        if (lmlist[12][2]<lmlist[11][2] and 
            lmlist[8][2]<lmlist[7][2]   and 
            lmlist[16][2]>lmlist[15][2] and 
            lmlist[20][2]>lmlist[19][2] and 
            lmlist[4][1]<lmlist[3][1]):

            return "I want Peace"
        return None

    def IsAbuse(self,img,lmlist):
        if (len(lmlist) == 0):
            return
        if (lmlist[12][2]<lmlist[11][2] and 
            lmlist[8][2]>lmlist[7][2]   and 
            lmlist[16][2]>lmlist[15][2] and 
            lmlist[20][2]>lmlist[19][2] and 
            lmlist[4][1]<lmlist[3][1]):

            return "Fuck You !"
        return None
    
    def IsHello(self,img, lmlist):
        if (len(lmlist) == 0):
            return
        if (lmlist[12][2]<lmlist[11][2] and 
            lmlist[8][2]<lmlist[7][2]   and 
            lmlist[16][2]<lmlist[15][2] and 
            lmlist[20][2]<lmlist[19][2] and 
            lmlist[4][1]>lmlist[3][1]):

            return "Hello!"
        return None

    def IsStop(self,img,lmlist):
        if (len(lmlist) == 0):
            return
        if (lmlist[12][2]>lmlist[11][2] and 
            lmlist[8][2]>lmlist[7][2]   and 
            lmlist[16][2]>lmlist[15][2] and 
            lmlist[20][2]>lmlist[19][2] and 
            lmlist[4][1]>lmlist[3][1]):

            return "Stop!!!"
        return None
    
    def IsThumbsUp(self, img, lmlist):
        if len(lmlist) == 0:
            return None

    

     
        

        if (lmlist[8][1] > lmlist[6][1] and   
        lmlist[12][1] > lmlist[10][1] and   
        lmlist[16][1] > lmlist[14][1] and  
        lmlist[20][1] > lmlist[18][1]and lmlist[4][2] < lmlist[3][2]):
            return "Thumbs up!"
    
        return None
