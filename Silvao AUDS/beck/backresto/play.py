import pyaudio
import wave
import sys
def playmusic(alista):
    file_path = alista
    wave_file = wave.open(file_path, 'rb')

    p = pyaudio.PyAudio()

    stream_out = p.open(format=p.get_format_from_width(wave_file.getsampwidth()),
                    channels=wave_file.getnchannels(),
                    rate=wave_file.getframerate(),
                    output=True)

    data = wave_file.readframes(1024)

    while data:
        stream_out.write(data)
        data = wave_file.readframes(1024)

    stream_out.stop_stream()
    stream_out.close()

    wave_file.close()

    p.terminate()