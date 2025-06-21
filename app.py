import streamlit as st
import requests

language = st.sidebar.selectbox("Select Language / اختر اللغة", ["English", "العربية"])

if language == "العربية":
    st.title("تحويل النص إلى كلام باستخدام ElevenLabs")
    text = st.text_area("أدخل النص لتحويله إلى كلام:")
    button_label = "تحويل إلى كلام"
else:
    st.title("Text to Speech with ElevenLabs")
    text = st.text_area("Enter text to convert to speech:")
    button_label = "Convert  Speech"

api_key = st.secrets["elevenlabs"]["api_key"]
voice_id = st.secrets["elevenlabs"]["voice_id"]


# Add dark mode toggle
if language == "العربية":
    dark_mode_label = "الوضع الداكن"
else:
    dark_mode_label = "Dark Mode"

dark_mode = st.sidebar.checkbox(dark_mode_label)

# Apply dark mode styling
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

if st.button(button_label):
    if not api_key or not text:
        if language == "العربية":
            st.error("مطلوب مفتاح API والنص.")
        else:
            st.error("API key and text are required.")
    else:
        headers = {
            "xi-api-key": api_key,
            "Content-Type": "application/json"
        }
        data = {
            "text": text,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
        }
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            st.audio(response.content, format="audio/mp3")
        else:
            if language == "العربية":
                st.error(f"خطأ: {response.status_code} - {response.text}")
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
