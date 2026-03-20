import numpy as np
import cv2
import os

# Output folder
os.makedirs("data", exist_ok=True)

WIDTH, HEIGHT = 512, 512

# Base noise
noise = np.random.rand(HEIGHT, WIDTH).astype(np.float32)

# Smooth noise to look like clouds
clouds = cv2.GaussianBlur(noise, (0, 0), sigmaX=20, sigmaY=20)

# Normalize to 0–255
clouds = cv2.normalize(clouds, None, 0, 255, cv2.NORM_MINMAX)
clouds = clouds.astype(np.uint8)

# Enhance contrast (important)
clouds = cv2.equalizeHist(clouds)

cv2.imwrite("data/cloud_density.png", clouds)

print("✅ cloud_density.png generated successfully")
