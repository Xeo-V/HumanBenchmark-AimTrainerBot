import cv2
import numpy as np
import pyautogui
import keyboard
x1, y1 = 0, 163  
x2, y2 = 1883, 692  
start = False
while True:
    if keyboard.is_pressed('o'):
        start = True  
    if keyboard.is_pressed('q'):
        break
    if start:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        roi = frame[y1:y2, x1:x2]
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        circles = cv2.HoughCircles(gray_roi, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=40, maxRadius=60)  
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                cv2.circle(roi, center, i[2], (0, 255, 0), 2)
                cv2.circle(roi, center, 2, (0, 0, 255), 3)
                pyautogui.click(x=center[0] + x1, y=center[1] + y1)
        cv2.imshow('ROI', roi)
        cv2.waitKey(1)

cv2.destroyAllWindows()
