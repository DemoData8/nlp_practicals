#pip3 install SpeechRecognition pydub

print("\n __By Mazhar Solkar\n")

import speech_recognition as sr
filename = "wavfile.wav"

#initialize the recognizer
r = sr.Recognizer()

#open the file
with sr.AudioFile(filename) as source:
    #listen for the data (load audio to memory)
    audio_data = r.record(source)
    #recongnize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)