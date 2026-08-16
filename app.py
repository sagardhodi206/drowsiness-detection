import cv2
import mediapipe as mp
import numpy as np
import winsound  # Built-in Windows library for audio alerts (Fallback available)

# -------------------------------------------------------------
# 1. INITIALIZE MEDIAPIPE FACE MESH & OPENCV
# -------------------------------------------------------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# MediaPipe Face Mesh Eye Landmark Indices
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# Drowsiness Hyperparameters
EAR_THRESHOLD = 0.22      # EAR below this value indicates closed eyes
CONSEC_FRAMES = 20        # Number of consecutive frames eyes must be closed to trigger alarm

counter = 0
alarm_on = False

def calculate_ear(eye_indices, landmarks, w, h):
    """Calculates the Eye Aspect Ratio (EAR) given eye landmark coordinates."""
    pts = np.array([[landmarks[idx].x * w, landmarks[idx].y * h] for idx in eye_indices])
    
    # Compute vertical eye distances
    v1 = np.linalg.norm(pts[1] - pts[5])
    v2 = np.linalg.norm(pts[2] - pts[4])
    
    # Compute horizontal eye distance
    h_dist = np.linalg.norm(pts[0] - pts[3])
    
    # EAR Formula
    ear = (v1 + v2) / (2.0 * h_dist)
    return ear

# Open Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # Flip horizontally for mirror view
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert frame to RGB for MediaPipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    status_text = "Status: Alert"
    status_color = (0, 255, 0)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark

            # -------------------------------------------------------------
            # 2. CALCULATE EYE ASPECT RATIO (EAR)
            # -------------------------------------------------------------
            left_ear = calculate_ear(LEFT_EYE, landmarks, w, h)
            right_ear = calculate_ear(RIGHT_EYE, landmarks, w, h)
            
            # Average EAR of both eyes
            avg_ear = (left_ear + right_ear) / 2.0

            # Check if eyes are closed
            if avg_ear < EAR_THRESHOLD:
                counter += 1
                if counter >= CONSEC_FRAMES:
                    status_text = "DROWSINESS ALERT!"
                    status_color = (0, 0, 255)
                    alarm_on = True
                    
                    # Trigger audible beep alarm (Windows specific)
                    try:
                        winsound.Beep(2500, 150)  # Frequency 2500Hz, Duration 150ms
                    except Exception:
                        print("\a")  # Terminal bell fallback for non-Windows OS
            else:
                counter = 0
                alarm_on = False

            # Display real-time EAR metric
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # -------------------------------------------------------------
    # 3. RENDER UI STATUS BANNER
    # -------------------------------------------------------------
    cv2.rectangle(frame, (20, 75), (320, 130), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, status_text, (30, 112),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    # Display video stream
    cv2.imshow("Drowsiness Face Detection", frame)

    # Press 'q' to exit application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()