import os

# Create 'data' folder and gesture class folders 0–5
for i in range(6):
    path = f"data/{i}"
    os.makedirs(path, exist_ok=True)

print("✅ Folders created: data/0 to data/5")
