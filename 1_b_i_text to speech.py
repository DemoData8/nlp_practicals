from playsound import playsound
from gtts import gTTS

myobj = gTTS(text="Welcome to Natural Language programming", lang="en", slow=False)
myobj.save("myfile.mp3")
playsound("myfile.mp3")

print("__By Mazhar Solkar")
