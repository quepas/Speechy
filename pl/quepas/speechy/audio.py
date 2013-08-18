__author__ = 'Quepas'

import pyaudio
import wave
import os

def record_wav(filename, lenght):
    chunk = 1024
    format = pyaudio.paInt16
    channels = 1
    rate = 12000
    record_seconds = lenght
    wave_output_filename = filename

    pyAudio = pyaudio.PyAudio()
    stream = pyAudio.open(format = format,
                          channels = channels,
                          rate = rate,
                          input=True,
                          frames_per_buffer = chunk)

    print("* recording [for %s seconds] *" % lenght)
    frames = []

    for i in range(0, int(rate/chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print ("* done recording *")

    stream.stop_stream()
    stream.close()
    pyAudio.terminate()

    wf = wave.open(wave_output_filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(pyAudio.get_sample_size(format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

# full filename
def convert_wav_to_flac(filename):
    os.system("flac -f %s" % filename)