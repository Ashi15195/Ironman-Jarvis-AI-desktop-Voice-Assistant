import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir ")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else:
        speak("good evening sir ")

    speak("I am Jarvis Sir how may i help you !")



def takeCommand(): #it takes microphone input return string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1 #for pause 1 sec
        audio = r.listen(source)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")


    except Exception as e:
        print("say that again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com',to ,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            speak(results)
            print(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")


        elif 'open code' in query:
            codePath = 
            os.startfile(codePath)

        elif 'email to Person' in query:
            try:
                speak("what should i say???")
                content = takeCommand()
                to = "xyz@gamil.com"
                sendEmail(to, content)
                speak("Email has been sent!!")
            except Exception as e:
                print(e)
                speak("sorry i am not able to send this email")



