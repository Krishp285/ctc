import numpy as np

def predict_rain(image):
    gray = np.mean(image, axis=2)
    brightness = np.mean(gray)

    if brightness > 170:
        return "High", "70%"
    elif brightness > 120:
        return "Moderate", "40%"
    else:
        return "Low", "15%"
