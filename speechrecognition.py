import speech_recognition as sr

def record_and_convert_to_text():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio_data = r.listen(source, timeout=10)

    text = r.recognize_google(audio_data)
    return text

