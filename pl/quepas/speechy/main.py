__author__ = 'Quepas'

from pl.quepas.speechy.audio import record_wav
from pl.quepas.speechy.audio import convert_wav_to_flac
from pl.quepas.speechy.recognition import speech_to_text

filePath = "output\out_file"
language = "en-US";

record_wav(filePath + ".wav", 3)
convert_wav_to_flac(filePath + ".wav")
print(speech_to_text(filePath + ".flac", language));


