import cv2
import numpy as np

def predict_next_frame(image):
    img = np.array(image)
    shifted = np.roll(img, shift=15, axis=1)
    blurred = cv2.GaussianBlur(shifted, (9, 9), 0)
    return blurred


def enhance_cloud_image(pil_img):
    img = np.array(pil_img)

    # Resize for clarity
    img = cv2.resize(img, (512, 512))

    # Increase contrast
    img = cv2.convertScaleAbs(img, alpha=2.0, beta=30)

    # Apply color map for visualization
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    colored = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

    return colored
