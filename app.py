import streamlit as st
from gtts import gTTS
import tempfile
import os

# Language selector as buttons
col1, col2 = st.columns(2)
language = "English"
if col1.button("English"):
    language = "English"
if col2.button("العربية"):
    language = "العربية"

if language == "العربية":
    st.title("تحويل النص إلى كلام")
    text = st.text_area("أدخل النص لتحويله إلى كلام:")
    button_label = "تحويل إلى كلام"
    tts_lang = "ar"
else:
    st.title("Text to Speech with gTTS")
    text = st.text_area("Enter text to convert to speech:")
    button_label = "Convert to Speech"
    tts_lang = "en"

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
