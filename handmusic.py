import handtrackingmodule as htm
import cv2
from pygame import mixer

cam = cv2.VideoCapture(0)

res = htm.handtrackingmodule()

finger_tip = [4, 8, 12, 16, 20]

hand_symbols = [[0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1], [1, 1, 0, 0, 0], [1, 1, 1, 0, 0],
                [1, 1, 1, 1, 0]]

pattern_temp = []

while True:
    _, img = cam.read()
    res.handtrack(img)
    points = res.handpoints(img)
    if len(points)>0:
        pattern = []
        if points[finger_tip[0]][1] > points[finger_tip[0]-2][1]:
            pattern.append(1)
        else:
            pattern.append(0)
        for finger in range(1,5):
            if points[finger_tip[finger]][2] < points[finger_tip[finger]-2][2]:
                pattern.append(1)
            else:
                pattern.append(0)
        if pattern_temp != pattern:
            pattern_temp = pattern
            for hand_symbol in hand_symbols:
                if pattern == hand_symbol:
                    file = f"{hand_symbols.index(hand_symbol)+1}.wav"
                    mixer.init()
                    mixer.music.load(file)
                    mixer.music.play()
                    print(pattern)
    cv2.imshow("img",img)
    KEY = cv2.waitKey(1)
    if KEY == ord("e"):
        break
cv2.destroyAllWindows()
cam.release()
