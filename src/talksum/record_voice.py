import sounddevice as sd
import wave
import tempfile

def record_audio(duration=5, sample_rate=44100, channels=2):
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait until recording is finished

    # Create a temporary file to store the recording
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix='recorded_')
    audio_path = temp_file.name

    # Save the recording in a WAV file
    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sd.default.dtype['int16'].itemsize)  # Size of data
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

    print(f"Recording finished: {audio_path}")
    return audio_path
