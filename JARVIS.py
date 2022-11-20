import pyttsx3          # for use to speak program
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser    #to open any website from this module
import os            # to use operating system's function
import smtplib       #for sending email function



engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voice')
engine.setProperty('voice',voice[1])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")

    elif hour>=12 and hour<18:
        speak("Good afternoon ")

    else:
        speak("Good evening")

    speak("I am jarvis... how may I help you sir..")

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gamil.com",587)
    server.ehlo()
    server.starttls()
    server.login("your email","your password(you can store in txt file)")
    server.sendmail("your email", to , content)
    server.close()



def takecommand():
    #it takes microphone input from the user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("please say that again.....")
        return "none"
    return query
if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching wikipedia...")
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")

            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'E:\music'
            songs = os.listdir(music_dir)
            print(songs[2])     #use random for random songs
            os.startfile(os.path.join(music_dir,songs[2]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strtime)
            speak(f"the time is {strtime}")

        elif 'open whatsapp' in query:
            app_path = "C:\\Users\\it care\\AppData\\Local\\WhatsApp\\WhatsApp.exe"     #use \\ for escape \
            os.startfile(app_path)

        elif 'email to harry' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "second_person_gmail.com"
                sendEmail(to,content)
                speak("email has been sent ")

            except Exception as e:
                print(e)
                speak("sorry sir... i am not able to send email for this time")

        elif 'stop the program' in query:
            print("ok... Have a nice day sir")
            speak("ok... Have a nice day sir")

            break
