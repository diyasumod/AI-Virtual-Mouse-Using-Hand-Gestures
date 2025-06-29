import cv2
import mediapipe as mp
import pyautogui
import time


global mouse_tipX
global mouse_tipY

delay_time = 0.1

def Draw_finger_points():
    for i in range(5):
        # Draw landmarks on the hand(s).
        cv2.circle(frame, 
                   (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                    int(hand_landmarks.landmark[i].y * frame.shape[0])),
                   5, (255, 0, 0), -1)

    for i in range(5,9):
        # Draw landmarks on the hand(s).
        cv2.circle(frame, 
                   (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                    int(hand_landmarks.landmark[i].y * frame.shape[0])),
                   5, (0, 255, 0), -1)

    for i in range(9,13):
        # Draw landmarks on the hand(s).
        cv2.circle(frame, 
                   (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                    int(hand_landmarks.landmark[i].y * frame.shape[0])),
                   5, (0, 255, 255), -1)

    for i in range(13,17):
        # Draw landmarks on the hand(s).
        cv2.circle(frame, 
                   (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                    int(hand_landmarks.landmark[i].y * frame.shape[0])),
                   5, (0, 0, 255), -1)

    for i in range(17,21):
        # Draw landmarks on the hand(s).
        cv2.circle(frame, 
                   (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                    int(hand_landmarks.landmark[i].y * frame.shape[0])),
                   5, (255, 0, 255), -1)


def move_cursor():
    try:
        tipX=hand_landmarks.landmark[8].x
        tipY=hand_landmarks.landmark[8].y

        if(tipX<0.21):
            tipX=0.01
        elif(tipX>0.8):
            tipX=0.99
        else:
            (tipX-0.2)*1.16


        if(tipY<0.31):
            tipY=0.01
        elif(tipY>0.9):
            tipY=0.99
        else:
            (tipY-0.3)*1.16
            
        global mouse_tipX
        global mouse_tipY

        mouse_tipX = int(tipX*1920)
        mouse_tipY = int(tipY*1080)

        pyautogui.moveTo(mouse_tipX,mouse_tipY,duration=.001)
        time.sleep(delay_time)

        #print(f'tipX={tipX}, tipY={tipY},mouse_tipX={mouse_tipX}, mouse_tipY={mouse_tipY}')
       
    except:
        print(f'move cursor position, {mouse_tipX},{mouse_tipY}')

import math

def calculate_distance(x1, y1, x2, y2):
        
    # Calculate the squared differences between x and y coordinates
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate the square root of the sum of squared differences
    distance = math.sqrt(dx**2 + dy**2)
    
    return distance

def drag_fun():
    x1=hand_landmarks.landmark[4].x* frame.shape[1]
    y1=hand_landmarks.landmark[4].y* frame.shape[0]

    x2=hand_landmarks.landmark[16].x* frame.shape[1]
    y2=hand_landmarks.landmark[16].y* frame.shape[0]

    click_dis = calculate_distance(x1, y1, x2, y2)
    print(f'click_dis:{click_dis}')
 
    
    if(click_dis<40):
        pyautogui.mouseDown()
        pyautogui.moveTo(mouse_tipX, mouse_tipY, duration=1)
        time.sleep(delay_time)
        print(f'Drag')
    elif(click_dis<80):
        pyautogui.mouseUp()
        
def scroll_fun():
    x1=hand_landmarks.landmark[4].x* frame.shape[1]
    y1=hand_landmarks.landmark[4].y* frame.shape[0]

    x2=hand_landmarks.landmark[20].x* frame.shape[1]
    y2=hand_landmarks.landmark[20].y* frame.shape[0]

    click_dis = calculate_distance(x1, y1, x2, y2)
    print(f'click_dis:{click_dis}')
 
    
    if(click_dis<40):
        pyautogui.scroll(10)
        print(f'scroll')
        
def single_click():
    x1=hand_landmarks.landmark[4].x* frame.shape[1]
    y1=hand_landmarks.landmark[4].y* frame.shape[0]

    x2=hand_landmarks.landmark[8].x* frame.shape[1]
    y2=hand_landmarks.landmark[8].y* frame.shape[0]

    click_dis = calculate_distance(x1, y1, x2, y2)
    print(f'click_dis:{click_dis}')
 
    
    if(click_dis<40):
        pyautogui.click(mouse_tipX,mouse_tipY)
        print(f'single click')
        

def double_click():
    x1=hand_landmarks.landmark[8].x* frame.shape[1]
    y1=hand_landmarks.landmark[8].y* frame.shape[0]

    x2=hand_landmarks.landmark[12].x* frame.shape[1]
    y2=hand_landmarks.landmark[12].y* frame.shape[0]

    click_dis = calculate_distance(x1, y1, x2, y2)
    print(f'click_dis:{click_dis}')
 
    
    if(click_dis<40):
        pyautogui.doubleClick(mouse_tipX,mouse_tipY)
        print(f'Double click')

def right_click():
    x1=hand_landmarks.landmark[4].x* frame.shape[1]
    y1=hand_landmarks.landmark[4].y* frame.shape[0]

    x2=hand_landmarks.landmark[12].x* frame.shape[1]
    y2=hand_landmarks.landmark[12].y* frame.shape[0]

    click_dis = calculate_distance(x1, y1, x2, y2)
    print(f'click_dis:{click_dis}')
 
    
    if(click_dis<40):
        pyautogui.rightClick(mouse_tipX,mouse_tipY)
        print(f'right click')

                
# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize Video Capture.
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
s=frame.shape
print(s)


while cap.isOpened():
    # Read frame from the camera.
    ret, frame = cap.read()
    # Flip the image horizontally
    frame = cv2.flip(frame, 1)

    if not ret:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands.
    results = hands.process(rgb_frame)

    # Check if hand(s) detected.
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            Draw_finger_points()
            move_cursor()

            single_click()
            double_click()
            right_click()
            scroll_fun()
            drag_fun()
            

    # Display the resulting frame.
    cv2.imshow('Hand Tracking', frame)

    # Press 'q' to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources.
cap.release()
cv2.destroyAllWindows()
