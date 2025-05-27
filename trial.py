import speech_recognition as sr
import pyttsx3
import whisper
from ffmpeg import *


#print(whisper.available_models())
model=whisper.load_model('base')
try:
    transcription=model.transcribe('harvard.wav',fp16=False)

except:
    ffmpeg_download()
    transcription=model.transcribe('harvard.wav')

print(transcription['text'])





    


