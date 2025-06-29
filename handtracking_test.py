import cv2
import mediapipe as mp

# Initialize MediaPipe Hands.
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize Video Capture.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Read frame from the camera.
    ret, frame = cap.read()
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
            for i in range(21):
                # Draw landmarks on the hand(s).
                cv2.circle(frame, 
                           (int(hand_landmarks.landmark[i].x * frame.shape[1]), 
                            int(hand_landmarks.landmark[i].y * frame.shape[0])),
                           5, (255, 0, 0), -1)

    # Display the resulting frame.
    cv2.imshow('Hand Tracking', frame)

    # Press 'q' to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources.
cap.release()
cv2.destroyAllWindows()
