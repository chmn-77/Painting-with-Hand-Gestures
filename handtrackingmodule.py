import cv2
import mediapipe as mp

class handtrackingmodule:
    def __init__(self):
        """self.cam = cv2.VideoCapture(0)
        while True:
            _, self.img = self.cam.read()
            cv2.imshow("img", self.img)
            self.KEY = cv2.waitKey(1)
            if self.KEY == ord("e"):
                break
        cv2.destroyAllWindows()
        self.cam.release()"""
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_drawing_utils = mp.solutions.drawing_utils

    def handtrack(self, img, draw_landmark=True):
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_img)
        self.rmhl = result.multi_hand_landmarks
        if self.rmhl:
            for hand_landmark in self.rmhl:
                if draw_landmark:
                    self.mp_drawing_utils.draw_landmarks(img, hand_landmark, self.mp_hands.HAND_CONNECTIONS)

    def handpoints(self, img):
        points = []
        if self.rmhl:
            handno = self.rmhl[0]
            for id, lm in enumerate(handno.landmark):
                h, w, c = img.shape
                x, y = int(lm.x*w), int(lm.y*h)
                points.append([id,x,y])
        return points