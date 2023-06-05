#pip3 install SpeechRecognition pydub

import speech_recognition as sr

#initialize the recognizer
r = sr.Recognizer()

#open the file
with sr.AudioFile("wavfile.wav") as source:
    text = r.recognize_google(r.record(source))
    print(text)
