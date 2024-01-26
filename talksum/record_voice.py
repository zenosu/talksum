import tempfile
import wave

import numpy as np
import sounddevice as sd


def record_audio(duration: int = 5, sample_rate: int = 44100, channels: int = 2) -> np.ndarray:
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()  # Wait until recording is finished
    return audio_data

def create_temp_file() -> str:
    # Create a temporary file to store the recording
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav', prefix='recorded_')
    return temp_file.name

def save_recording(audio_data: np.ndarray, audio_path: str, sample_rate: int, channels: int) -> None:
    # Save the recording in a WAV file
    with wave.open(audio_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sd.default.dtype['int16'].itemsize)  # Size of data
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def record_and_save_audio(duration: int = 5, sample_rate: int = 44100, channels: int = 2) -> str:
    audio_data = record_audio(duration, sample_rate, channels)
    audio_path = create_temp_file()
    save_recording(audio_data, audio_path, sample_rate, channels)
    print(f"Recording finished: {audio_path}")
    return audio_path
