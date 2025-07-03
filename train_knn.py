import os
import cv2
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier

# Settings
IMG_SIZE = 64
X = []
y = []

print("📂 Loading gesture images...")

for label in os.listdir("data"):
    folder_path = os.path.join("data", label)
    for file in os.listdir(folder_path):
        img_path = os.path.join(folder_path, file)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
        X.append(img.flatten())
        y.append(int(label))

X = np.array(X)
y = np.array(y)

print(f"✅ Loaded {len(X)} images. Training KNN...")

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save model
with open("gesture_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as gesture_model.pkl")
