import pytest
from unittest.mock import patch, MagicMock
from src.talksum.record_voice import record_audio

@patch('src.talksum.record_voice.sd')
@patch('src.talksum.record_voice.wave')
@patch('src.talksum.record_voice.tempfile')
def test_record_audio(mock_tempfile, mock_wave, mock_sd):
    # Mock the sounddevice.rec() function
    mock_sd.rec.return_value = 'audio_data'
    
    # Mock the tempfile.NamedTemporaryFile() function
    mock_tempfile.NamedTemporaryFile.return_value.name = 'temp_file.wav'
    
    # Call the function to test
    audio_path = record_audio()
    
    # Assert that the function calls are made correctly
    mock_sd.rec.assert_called_once()
    mock_sd.wait.assert_called_once()
    mock_tempfile.NamedTemporaryFile.assert_called_once()
    mock_wave.open.assert_called_once_with('temp_file.wav', 'wb')
    
    # Assert that the function returns the correct audio path
    assert audio_path == 'temp_file.wav'
