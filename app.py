import streamlit as st
from gtts import gTTS
import tempfile
import os

# Language selection using session state
if "language" not in st.session_state:
    st.session_state.language = "English"

col1, col2 = st.columns(2)
if col1.button("English"):
    st.session_state.language = "English"
if col2.button("العربية"):
    st.session_state.language = "العربية"

language = st.session_state.language

# Set language for gTTS
tts_lang = "en"

if language == "العربية":
    st.title("تحويل النص إلى كلام")
    text = st.text_area("أدخل النص لتحويله إلى كلام:")
    button_label = "تحويل إلى كلام"
else:
    st.title("Text to Speech")
    text = st.text_area("Enter text to convert to speech:")
    button_label = "Convert to Speech"

if st.button(button_label):
    if not text.strip():
        st.error("Please enter some text." if language == "English" else "من فضلك أدخل نصًا.")
    else:
        try:
            tts = gTTS(text, lang=tts_lang, slow=False)
            # Use temporary file with suffix .mp3
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as fp:
                temp_path = fp.name
                tts.save(temp_path)

            # Read audio file after saving and close it before playback
            with open(temp_path, "rb") as audio_file:
                audio_bytes = audio_file.read()

            st.audio(audio_bytes, format="audio/mp3")

            # Delete temp file after playback
            os.remove(temp_path)

        except Exception as e:
            st.error(f"An error occurred: {e}")
