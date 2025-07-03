import cv2
import pickle
import numpy as np

# Load trained model
with open("gesture_model.pkl", "rb") as f:
    model = pickle.load(f)

IMG_SIZE = 64

cap = cv2.VideoCapture(0)
print("\n🖐️ Show your hand in the box. Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    x, y, w, h = 100, 100, 300, 300
    roi = frame[y:y+h, x:x+w]
    roi_gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    roi_resized = cv2.resize(roi_gray, (IMG_SIZE, IMG_SIZE)).flatten().reshape(1, -1)

    # Predict gesture
    prediction = model.predict(roi_resized)[0]
    
    # Draw box and result
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(frame, f"Gesture: {prediction}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
