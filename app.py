import streamlit as st
from gtts import gTTS
import os

st.set_page_config(page_title="Text to Speech", page_icon="🔊", layout="centered")

st.title("🔊 Teks ke Suara Online")
st.write("Masukkan teks di bawah, lalu dengarkan hasilnya!")

# Input dari pengguna
text = st.text_area("📝 Masukkan Teks Anda di sini", height=150)

# Tombol konversi
if st.button("🔁 Ubah Jadi Suara"):
    if text.strip() == "":
        st.warning("Teks tidak boleh kosong.")
    else:
        # Konversi teks jadi audio pakai gTTS
        tts = gTTS(text)
        tts.save("output.mp3")

        # Tampilkan audio player
        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()
        st.success("✅ Berhasil dikonversi! Dengarkan di bawah:")
        st.audio(audio_bytes, format="audio/mp3")
