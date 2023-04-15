import cv2
import mediapipe as mp
from test import handTracker 


def mark(image, x, y):
    cv2.circle(image, (x, y), 15, (255, 255, 255), thickness=-1)
    
def main():
    cap = cv2.VideoCapture(0)
    tracker = handTracker()
    drawList = []
    
    while True:
        success,image = cap.read()
        image = cv2.resize(image, (1000, 750))

        image = tracker.handsFinder(image, draw=False)
        lmList = tracker.positionFinder(image, draw=False)

        if len(lmList) != 0:
            grab = ((lmList[4][1]-lmList[8][1])**2 + (lmList[4][2] - lmList[8][2])**2)
            clear = ((lmList[4][1]-lmList[20][1])**2 + (lmList[4][2] - lmList[20][2])**2)
            if grab < 5000:
                drawList.append([lmList[8][1], lmList[8][2]])

            if clear < 1000:
                drawList = []
        if len(drawList)>1:
            for i in range(1,len(drawList)):
                cv2.line(image,
            pt1=(drawList[i-1][0], drawList[i-1][1]),
            pt2=(drawList[i][0], drawList[i][1]),
            color=(0, 255, 0),
            thickness=3,
            lineType=cv2.LINE_4,
            shift=0)
                # mark(image, drawList[i][0], drawList[i][1])
        image = cv2.flip(image, 1)

        cv2.imshow("Video",image)
        key = cv2.waitKey(1)
        if key == 27:
            break

if __name__ == "__main__":
    main()