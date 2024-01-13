import torch
from torchaudio.pipelines import TACOTRON2_GRIFFINLIM_PHONE_LJSPEECH

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the TACOTRON2_GRIFFINLIM_PHONE_LJSPEECH bundle
bundle = TACOTRON2_GRIFFINLIM_PHONE_LJSPEECH

# Get the text processor, tacotron2, and vocoder
processor = bundle.get_text_processor()
tacotron2 = bundle.get_tacotron2().to(device)
vocoder = bundle.get_vocoder().to(device)

# Function to generate audio
def generate_audio(text):
    with torch.inference_mode():
        processed, lengths = processor(text)
        processed = processed.to(device)
        lengths = lengths.to(device)
        spec, spec_lengths, _ = tacotron2.infer(processed, lengths)
        waveforms, lengths = vocoder(spec, spec_lengths)
    return waveforms

# Streamlit app
st.title("Text-to-Speech with Streamlit")

# Text input for user input
text_input = st.text_input("Enter text:", "Hello, this is a test.")

# Button to generate and play audio
if st.button("Generate and Play Audio"):
    # Generate audio
    audio_data = generate_audio(text_input)

    # Play audio using streamlit
    st.audio(audio_data.squeeze().cpu().numpy(), format="audio/wav", sample_rate=vocoder.sample_rate)

