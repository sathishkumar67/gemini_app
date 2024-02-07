import requests

API_URL = "https://api-inference.huggingface.co/models/facebook/fastspeech2-en-ljspeech"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


# audio, sampling_rate = query({
#     "inputs": "The answer to the universe is 42",
# })


audio= query({
    "inputs": "The answer to the universe is 42",
})
# print(audio)
# You can access the audio with IPython.display for example
from IPython.display import Audio

Audio(audio, rate=22050)