import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
from main import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak("Good Morning ankur")
    
    elif hour >= 13 and hour <=16:
        speak("Good Afternoon ankur")

    else:
        speak("Good Evening ankur")

    speak("this is jarvis version one point o, booting up your suit.")
    print("Booting completed ! Let's get started .... [To stop at any time , just say exit or bye jarvis] ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to your command .....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing .... ")
        query = r.recognize_google(audio , language='en-in')
        print("You are saying --> {}".format(query.lower()))

    except Exception as e:
        print("Say that again sir .. I am still Learning..\n")
        speak("Say that again sir .. I am still Learning..")
        return "None"

    return query

if __name__ == "__main__":
    wishMe()
    
query = ''    
while(True):
    query = takeCommand().lower()
    if 'hello' in query:
        print("Hello sir , its lovely weather in your city.")
        speak("Hello sir , its lovely weather in your city.")
        continue
    
    elif 'who are you' in query:
        speak("Are you serious ?")
        ans = tellMe()
        speak(ans)

    elif 'avengers assemble' in query:
        speak("Avengers assemble executed successfully")
        avengersAssemble()

    elif 'open google' in query:
        speak("Opening Google")
        openGoogle()
    
    elif 'show me your face' in query:
         speak("Powering up my mechanics ..  Get ready to see my holographic face .. ")
         faceReveal()

    elif 'open youtube' in query:
        speak("Opening youtube")
        openYoutube()

    elif 'kill all' in query:
        speak("I am not made to kill buddy .. i only kill people with my swag")
        speak("This is my thug life")

    elif 'ninja' in query:
        speak(" o mee go ")
        openChannelJsFilms()

    elif 'play music' in query:
        speak("Playing your favourite songs sir...")
        playMusic()
    
    elif 'battery' in query:
        answer = batteryCheckup()
        print(answer)
        speak(answer)

    elif 'exit' in query:
        print("Signing off ! If you need me , Remember I am just a touch away . \nStay safe")
        speak("Signing off . If you need me , remember i am just a touch away . Stay safe")
        break
        
            