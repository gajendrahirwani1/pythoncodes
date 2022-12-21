import pyttsx3
engine = pyttsx3.init()
while(True):
    print("enter any sentence")
    lyrics = input()
    engine.say(lyrics)
    engine.runAndWait()
