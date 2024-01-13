import google.generativeai as genai
from settings import generation_config, safety_settings

genai.configure(api_key="AIzaSyC-41AjM3RwreirqtPNJT-NCGqo6W-DHGk")

gemini_pro_text = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)