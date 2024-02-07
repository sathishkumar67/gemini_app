import streamlit as st
from PIL import Image
from image import image_to_binary
from speechrecognition import record_and_convert_to_text
from gemini_pro import gemini_pro_text, gemini_pro_vision


st.set_page_config(
    page_title="Gemini Pro",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

sidebar = st.sidebar

option = sidebar.selectbox(
    'Choose the Model:',
    ("Gemini Pro Text", "Gemini Pro Vision")
)

if option == "Gemini Pro Text":

    prompt_text = st.chat_input("Enter What you would like to Know")

    if prompt_text:
        response = gemini_pro_text.generate_content([prompt_text])
        st.write(response.text)

    elif st.button("Record Audio"):
        audio_text = record_and_convert_to_text()
        st.write(audio_text)
        response = gemini_pro_text.generate_content([audio_text])
        st.write(response.text)

elif option == "Gemini Pro Vision":
    uploaded_file = st.file_uploader("Choose an image...")
    prompt_image = st.chat_input("Enter the prompt for the image:")

    checkbox = st.sidebar.checkbox("view image")

    if checkbox:
        st.image(Image.open(uploaded_file))

    if (uploaded_file and prompt_image) is not None:
        image = Image.open(uploaded_file)
        binary_bytes = image_to_binary(image)
        image_parts = [
            {
                "mime_type": "image/jpeg" ,
                "data": binary_bytes
            },
        ]

        prompt_parts = [
            image_parts[0],
            prompt_image
        ]

        response = gemini_pro_vision.generate_content(prompt_parts)
        st.write(response.text)









