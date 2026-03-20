import streamlit as st
import numpy as np
import cv2

from fetcher import fetch_latest_image
from predictor import predict_next_frame, enhance_cloud_image
from rain_prediction import predict_rain

st.set_page_config("Chase the Cloud", "☁️", layout="wide")
st.title("☁️ Chase the Cloud – Dynamic Cloud Motion Prediction")

st.write("Click the button to fetch the latest satellite cloud image dynamically.")

if st.button("🌍 Fetch Latest Satellite Image"):

    with st.spinner("Fetching satellite image..."):
        raw_img = fetch_latest_image()
        enhanced_img = enhance_cloud_image(raw_img)


    if raw_img is None:
        st.error("Failed to fetch satellite image. Check internet connection.")
    else:
        st.success("Satellite image fetched successfully")

        st.image(enhanced_img, caption="Enhanced Cloud Density Map", use_container_width=True)

        predicted = predict_next_frame(raw_img)
        st.image(predicted, caption="Predicted Next Cloud Frame", use_container_width=True)

        level, prob = predict_rain(predicted)

        st.subheader("🌧️ Rain Prediction")
        st.write(f"**Rain Probability:** {prob}")
        st.write(f"**Rain Intensity:** {level}")
