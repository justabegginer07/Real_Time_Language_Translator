import speech_recognition as sr
import pyttsx3
import whisper
from ffmpeg import *
import os

os.environ['PATH']+=os.pathsep+os.path.abspath('.')

#print(whisper.available_models())
model=whisper.load_model('base')
ffmpeg_download()
transcription=model.transcribe('harvard.wav',fp16=False)
print(transcription['text'])





    


