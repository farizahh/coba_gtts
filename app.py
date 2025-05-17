import streamlit as st
from streamlit_webrtc import (
    WebRtcMode,
    webrtc_streamer,
    __version__ as st_webrtc_version,
)

from ultralytics import YOLO
import cv2
import av

# Load YOLOv8 model
model = YOLO("bisindo_yolov8.pt")  # Pastikan file .pt ada di folder yang sama

st.title("Pendeteksi Bahasa Isyarat BISINDO")
st.write("Menggunakan YOLOv8 + Streamlit WebRTC")

# Proses frame video
def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # Deteksi pakai YOLO
    results = model(img)
    annotated_frame = results[0].plot()

    return av.VideoFrame.from_ndarray(annotated_frame, format="bgr24")

# Tampilkan kamera dan deteksi
webrtc_ctx = webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    async_processing=True,
)


