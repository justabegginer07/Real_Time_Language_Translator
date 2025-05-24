import os
import speech_recognition as sr
import pyttsx3
import whisper
import requests
import tarfile

#print(whisper.available_models())
model=whisper.load_model('base')
transcription=model.transcribe('harvard.wav',fp16=False)
print(transcription['text'])



def ffmpeg_file(dest_folder='ffmpeg'):
    


