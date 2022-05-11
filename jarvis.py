# from nturl2path import url2pathname
import os
import random
from winsound import PlaySound

import pyttsx3
from datetime import *
import speech_recognition as sr
import webbrowser
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 120)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")
    speak("I'm x ,How may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Sorry! please say that again")
        return "None"
    return query


if __name__ == '__main__':
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices: 
        print("Voice:") 
        print("ID: %s" %voice.id) 
        print("Name: %s" %voice.name) 
        print("Age: %s" %voice.age) 
        print("Gender: %s" %voice.gender) 
        print("Languages Known: %s" %voice.languages)
    wishme()
    while True:
        query = takeCommand().lower()
        print(query)

        if 'wikipedia' in query:
            speak("seraching on  Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            print(result)
            speak(result)
        elif 'youtube' in query:
        #    while True:
            webbrowser.open("www.youtube.com")
            # PlaySound('')
            # webbrowser.open("https://www.youtube.com/song")
            # webbrowser.open("https://www.youtube.com/song")
        elif 'google' in query:
            webbrowser.open("Google.com")
        elif 'facebook' in query:
            webbrowser.open("facebook.com")
        elif 'instagram' in query:
            webbrowser.open("instagram.com")
        elif 'twitter' in query:
            webbrowser.open("twitter.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\DeLL\\Desktop\\songs1'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'the time' in query:
            strtime = datetime.now().strftime("%H:%M:%S")
            print(strtime)
            speak(f"Sir, The time is {strtime}")