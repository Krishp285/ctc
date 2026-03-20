import streamlit as st
import numpy as np
import cv2
from PIL import Image
import time

# ================= CONFIG =================
SIZE = (512, 512)
FRAMES = 6          # number of motion frames
SHIFT_STEP = 8      # pixels per frame
# =========================================

st.set_page_config("CloudCast – Cloud Motion", "☁️", layout="wide")
st.title("☁️ Chase the Cloud – Visible Cloud Motion")

# ---------- LOAD STATIC WORLD MAP ----------
def load_world_map():
    return Image.open("data/world_map.jpeg").convert("RGB").resize(SIZE)

# ---------- LOAD CLOUD IMAGE (GRAYSCALE) ----------
def load_cloud_image():
    img = Image.open("data/cloud_density.png").convert("L").resize(SIZE)
    return np.array(img)

# ---------- THERMAL COLOR ----------
def thermal_color(gray):
    colored = cv2.applyColorMap(gray, cv2.COLORMAP_JET)
    return cv2.cvtColor(colored, cv2.COLOR_BGR2RGB)

# ---------- OVERLAY ----------
def overlay(map_img, cloud_img, alpha=0.6):
    return np.clip(
        (1 - alpha) * map_img + alpha * cloud_img,
        0, 255
    ).astype(np.uint8)

# ---------- GENERATE MOTION FRAMES ----------
def generate_motion_frames(cloud_gray):
    frames = []
    for i in range(FRAMES):
        shifted = np.roll(cloud_gray, i * SHIFT_STEP, axis=1)
        frames.append(shifted)
    return frames

# ================= UI =================
if st.button("▶ Show Cloud Motion"):

    map_img = np.array(load_world_map())
    cloud_gray = load_cloud_image()

    motion_frames = generate_motion_frames(cloud_gray)

    placeholder = st.empty()

    for i, frame in enumerate(motion_frames):
        cloud_color = thermal_color(frame)
        final = overlay(map_img, cloud_color)

        placeholder.image(
            final,
            caption=f"Cloud Motion Frame {i+1}",
            use_container_width=True
        )

        time.sleep(0.6)

    st.success("Cloud motion animation completed")

else:
    st.info("Click the button to visualize cloud movement")
