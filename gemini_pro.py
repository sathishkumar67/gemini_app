import google.generativeai as genai
from settings import text_generation_config, text_safety_settings, vision_generation_config, vision_safety_settings

genai.configure(api_key="AIzaSyC-41AjM3RwreirqtPNJT-NCGqo6W-DHGk")

gemini_pro_text = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=text_generation_config,
                              safety_settings=text_safety_settings)


gemini_pro_vision = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=vision_generation_config,
                              safety_settings=vision_safety_settings)



