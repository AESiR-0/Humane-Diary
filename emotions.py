import speech_recognition as sr
import nltk
nltk.download('punkt')
import pandas as pd
from nltk import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import requests
from LeXmo import LeXmo
# import text2emotion as emotion

# # Read the audio file into an AudioFile object
def audio_emo(name):
    r = sr.Recognizer()
    with sr.AudioFile('D:\Humane Diary\\'+name) as source:
        audio = r.record(source)

    # # Transcribe the audio file using the recognize_google method
    transcript = r.recognize_google(audio)
    emo=LeXmo.LeXmo(transcript)
    return emo 
    
def text_emo(name, text):
    emo=LeXmo.LeXmo(text)
    return emo