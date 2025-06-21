import streamlit as st
from gtts import gTTS
import tempfile
import os

# Language selector
language = st.sidebar.selectbox("Select Language / اختر اللغة", ["English", "العربية"])

if language == "العربية":
    st.title("تحويل النص إلى كلام باستخدام gTTS")
    text = st.text_area("أدخل النص لتحويله إلى كلام:")
    button_label = "تحويل إلى كلام"
    tts_lang = "ar"
    dark_mode_label = "الوضع الداكن"
else:
    st.title("Text to Speech with gTTS")
    text = st.text_area("Enter text to convert to speech:")
    button_label = "Convert to Speech"
    tts_lang = "en"
    dark_mode_label = "Dark Mode"

# Dark mode toggle
dark_mode = st.sidebar.checkbox(dark_mode_label)

if dark_mode:
    st.markdown(
        """
        <style>
        body, .stApp, .css-18e3th9, .css-1d391kg {
            background-color: #181818 !important;
            color: #f1f1f1 !important;
        }
        .stTextInput > div > div > input, .stTextArea > div > textarea {
            background-color: #222 !important;
            color: #f1f1f1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Button clicked
if st.button(button_label):
    if not text.strip():
        st.error("Please enter some text." if language == "English" else "من فضلك أدخل نصًا.")
    else:
        try:
            tts = gTTS(text, lang=tts_lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                temp_path = fp.name
                tts.save(temp_path)
                audio_file = open(temp_path, "rb")
                audio_bytes = audio_file.read()
                st.audio(audio_bytes, format="audio/mp3")
                audio_file.close()
                os.remove(temp_path)
        except Exception as e:
            st.error(f"An error occurred: {e}")
