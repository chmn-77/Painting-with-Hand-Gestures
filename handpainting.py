import handtrackingmodule as htm
import cv2
import mediapipe as mp
import numpy as np
from collections import deque

cam = cv2.VideoCapture(0)
cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
cv2.namedWindow("paintWindow", cv2.WINDOW_NORMAL)

res = htm.handtrackingmodule()


violet_points = [deque(maxlen=512)]
indigo_points = [deque(maxlen=512)]
blue_points = [deque(maxlen=512)]
green_points = [deque(maxlen=512)]
yellow_points = [deque(maxlen=512)]
orange_points = [deque(maxlen=512)]
red_points = [deque(maxlen=512)]

violet_index = 0
indigo_index = 0
blue_index = 0
green_index = 0
yellow_index = 0
orange_index = 0
red_index = 0

colors = {"VIOLET": (255, 0, 143), "INDIGO": (130, 0, 75), "BLUE": (255, 0, 0), "GREEN": (0, 128, 0),
          "YELLOW": (0, 255, 255), "ORANGE": (0, 143, 255), "RED": (0, 0, 255), "WHITE": (255, 255, 255)}
current_color = "WHITE"
pen_down = False


paintWindow = np.zeros((700, 700, 3))+255
for iteration_x in range(70):
    for iteration_y in range(700):
        for iteration_z in range(3):
            paintWindow[iteration_x][iteration_y][iteration_z] = 0

paintWindow = cv2.rectangle(paintWindow, (10, 10), (60, 60), colors["RED"], -1)
paintWindow = cv2.rectangle(paintWindow, (70, 10), (120, 60), colors["VIOLET"], -1)
paintWindow = cv2.rectangle(paintWindow, (130, 10), (180, 60), colors["INDIGO"], -1)
paintWindow = cv2.rectangle(paintWindow, (190, 10), (240, 60), colors["BLUE"], -1)
paintWindow = cv2.rectangle(paintWindow, (250, 10), (300, 60), colors["GREEN"], -1)
paintWindow = cv2.rectangle(paintWindow, (310, 10), (360, 60), colors["YELLOW"], -1)
paintWindow = cv2.rectangle(paintWindow, (370, 10), (420, 60), colors["ORANGE"], -1)
paintWindow = cv2.rectangle(paintWindow, (430, 10), (480, 60), colors["WHITE"], 2)
cv2.putText(paintWindow, "RED", (25, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "VIOLET", (80, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "INDIGO", (140, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (203, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (260, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (318, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "ORANGE", (377, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
cv2.putText(paintWindow, "CLEAR", (440, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)



def menu_list(x , current_color):
    if 10 <= x <= 60:
        return "RED"
    elif 70 <= x <= 120:
        return "VIOLET"
    elif 130 <= x <= 180:
        return "INDIGO"
    elif 190 <= x <= 240:
        return "BLUE"
    elif 250 <= x <= 300:
        return "GREEN"
    elif 310 <= x <= 360:
        return "YELLOW"
    elif 370 <= x <= 420:
        return "ORANGE"
    elif 430 <= x <= 480:
        return "CLEAR"
    else:
        return current_color

while True:
    x, y = 0, 0
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    res.handtrack(frame)
    frame = cv2.rectangle(frame, (10, 10), (60, 60), colors["RED"], -1)
    frame = cv2.rectangle(frame, (70, 10), (120, 60), colors["VIOLET"], -1)
    frame = cv2.rectangle(frame, (130, 10), (180, 60), colors["INDIGO"], -1)
    frame = cv2.rectangle(frame, (190, 10), (240, 60), colors["BLUE"], -1)
    frame = cv2.rectangle(frame, (250, 10), (300, 60), colors["GREEN"], -1)
    frame = cv2.rectangle(frame, (310, 10), (360, 60), colors["YELLOW"], -1)
    frame = cv2.rectangle(frame, (370, 10), (420, 60), colors["ORANGE"], -1)
    frame = cv2.rectangle(frame, (430, 10), (480, 60), colors["WHITE"], 2)
    cv2.putText(frame, "CLEAR", (440, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "VIOLET", (80, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "INDIGO", (140, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (203, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (260, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (318, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "ORANGE", (377, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    cv2.putText(frame, "RED", (25, 38), cv2.FONT_HERSHEY_SIMPLEX, 0.3, colors["WHITE"], 1, cv2.LINE_AA)
    points = res.handpoints(frame)
    if len(points)>0:
        x, y = points[8][1], points[8][2]
        if points[4][1] < points[2][1]:
            pen_down = False
        else:
            pen_down = True
    if pen_down:
        if y <= 78:
            selected_menu = menu_list(x, current_color)
            if selected_menu == "CLEAR":

                violet_points = [deque(maxlen=512)]
                indigo_points = [deque(maxlen=512)]
                blue_points = [deque(maxlen=512)]
                green_points = [deque(maxlen=512)]
                yellow_points = [deque(maxlen=512)]
                orange_points = [deque(maxlen=512)]
                red_points = [deque(maxlen=512)]

                violet_index = 0
                indigo_index = 0
                blue_index = 0
                green_index = 0
                yellow_index = 0
                orange_index = 0
                red_index = 0

                paintWindow[70:,:,:] = 255

            else:
                current_color = selected_menu

        else:
            if current_color == "VIOLET":
                violet_points[violet_index].appendleft((x, y))
            elif current_color == "INDIGO":
                indigo_points[indigo_index].appendleft((x, y))
            elif current_color == "BLUE":
                blue_points[blue_index].appendleft((x, y))
            elif current_color == "GREEN":
                green_points[green_index].appendleft((x, y))
            elif current_color == "YELLOW":
                yellow_points[yellow_index].appendleft((x, y))
            elif current_color == "ORANGE":
                orange_points[orange_index].appendleft((x, y))
            elif current_color == "RED":
                red_points[red_index].appendleft((x, y))
    else:
        violet_points.append(deque(maxlen=512))
        violet_index += 1
        indigo_points.append(deque(maxlen=512))
        indigo_index += 1
        blue_points.append(deque(maxlen=512))
        blue_index += 1
        green_points.append(deque(maxlen=512))
        green_index += 1
        yellow_points.append(deque(maxlen=512))
        yellow_index += 1
        orange_points.append(deque(maxlen=512))
        orange_index += 1
        red_points.append(deque(maxlen=512))
        red_index += 1

    colored_points = {"VIOLET": violet_points, "INDIGO": indigo_points, "BLUE": blue_points, "GREEN": green_points,
                      "YELLOW": yellow_points, "ORANGE": orange_points, "RED": red_points}
    for i in colored_points:
        for j in range(len(colored_points[i])):
            len_of_dequeList = len(colored_points[i][j])
            for k in range(1,len_of_dequeList):
                if colored_points[i][j][k-1] is None or colored_points[i][j][k] is None:
                    continue
                cv2.line(paintWindow, colored_points[i][j][k-1], colored_points[i][j][k], colors[i],20)

    cv2.circle(frame, (x, y), 10, [0, 0, 255], -1)
    #cv2.circle(paintWindow, (x, y), 10, [0, 0, 255], -1)
    cv2.putText(frame, str(x) + " " + str(y), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (176, 255, 156), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("paintWindow", paintWindow)
    key = cv2.waitKey(1)
    if key == ord("e"):
        break
cv2.destroyAllWindows()
cam.release()
