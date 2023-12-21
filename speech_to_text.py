from transformers import pipeline, Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# Load the pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

# Create a speech-to-text pipeline
asr_pipeline = pipeline("automatic-speech-recognition", model=model, tokenizer=tokenizer)

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return asr_pipeline(audio_bytes).get('text')
