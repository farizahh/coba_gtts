import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode
from ultralytics import YOLO
import av

# Cache/load model
cache_key = "yolov8_model"
if cache_key in st.session_state:
    model = st.session_state[cache_key]
else:
    model = YOLO("bisindo_yolov8.pt")
    st.session_state[cache_key] = model

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    result = st.session_state[cache_key](img)[0]
    annotated = result.plot()
    return av.VideoFrame.from_ndarray(annotated, format="bgr24")

webrtc_streamer(
    key="object-detection",
    mode=WebRtcMode.SENDRECV,
    video_frame_callback=video_frame_callback,
    media_stream_constraints={"video": True, "audio": False},
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    async_processing=True,
)
