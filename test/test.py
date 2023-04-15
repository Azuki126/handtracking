import cv2
import mediapipe as mp

class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    def handsFinder(self,image,draw=True):
        imageRGB = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imageRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(image, handLms, self.mpHands.HAND_CONNECTIONS)
        return image
    
    def positionFinder(self,image, handNo=0, draw=False):
        lmlist = []
        if self.results.multi_hand_landmarks:
            Hand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(Hand.landmark):
                h,w,c = image.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id,cx,cy])
            if draw:
                cv2.circle(image,(lmlist[8][1],lmlist[8][2]), 15 , (255,0,255), cv2.FILLED)
                # cv2.circle(image,(lmlist[20][1],lmlist[20][2]), 15 , (255,0,255), cv2.FILLED)

        return lmlist


def main():
    cap = cv2.VideoCapture(0)
    tracker = handTracker()
    turtle = cv2.imread("test/jishaku.jpg")
    turtle = cv2.resize(turtle, (125,125))
    x=500
    y=375
    while True:
        success,image = cap.read()
        image = cv2.resize(image, (1000, 750))

        image = tracker.handsFinder(image)
        lmList = tracker.positionFinder(image)
        if len(lmList) != 0:
            print(lmList[4])
        if len(lmList) != 0:
            grab = ((lmList[4][1]-lmList[8][1])**2 + (lmList[4][2] - lmList[8][2])**2)
            if grab < 5000:
                y = (lmList[5][2] + lmList[0][2])//2 - 150
                x = (lmList[5][1] + lmList[0][1])//2
                # if (y1-y)**2 + (x1-x)**2 < 5000:
                #     y = y1
                #     x = x1

        image[y:y+125, x:x+125] = turtle

        image = cv2.flip(image, 1)

        cv2.imshow("Video",image)
        key = cv2.waitKey(1)
        if key == 27:
            break
if __name__ == "__main__":
    main()