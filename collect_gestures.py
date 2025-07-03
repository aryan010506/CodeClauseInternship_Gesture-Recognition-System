import cv2
import os

# Ask user for gesture label (0–5)
gesture_id = input("Enter gesture label (0–5): ")
save_path = f"data/{gesture_id}"
os.makedirs(save_path, exist_ok=True)
11
cap = cv2.VideoCapture(0)
count = len(os.listdir(save_path))  # Continue count if already has images

print("\n🖐️ Show your gesture in the box and press 's' to save. Press 'q' to quit.\n")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip camera for mirror view
    frame = cv2.flip(frame, 1)

    # Define Region of Interest (ROI) box
    x, y, w, h = 100, 100, 300, 300
    roi = frame[y:y+h, x:x+w]
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display info
    cv2.putText(frame, f"Images Saved: {count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Collect Gesture", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        # Save captured image
        img_name = f"{save_path}/img_{count}.jpg"
        cv2.imwrite(img_name, roi)
        print(f"[+] Saved: {img_name}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
