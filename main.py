import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r=sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        print("listening . . .")
        voice_data=""
        try:
            audio=r.listen(source,15,5)
            voice_data=r.recognize_google(audio)
            print(voice_data)
        except sr.WaitTimeoutError:
            speak("Wait time out error")
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my speech server is down")
        return voice_data

def speak(audio_string):
    tts=gTTS(text=audio_string, lang="en")
    r = random.randint(1,1000000)
    audio_file="audio-"+str(r)+".mp3"
    tts.save(audio_file)
    print(audio_string)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def respond(voice_data):
    if "what" in voice_data:
        if "your" and "name" in voice_data:
            speak("My name is Alexa")
            return
        if "time" in voice_data:
            speak(ctime())
            return
    if "search" in voice_data or "find" in voice_data or "google" in voice_data :
        if "location" in voice_data or "where" in voice_data : 
            location=record_audio("What is the location name?")
            if location=="" :
                return
            url="https://google.nl/maps/place/" + location + "/&amp"
            webbrowser.get().open(url)
            speak("Here is the location of "+ location)
            return
        else:
            search=record_audio("What do you want me to search for?")
            if search=="" :
                return
            url="https://www.google.com/search?q=" + search
            webbrowser.get().open(url)
            speak("Here is what I found for "+ search)
            return    
    if "exit" in voice_data:
        speak("Good Bye! Have a nice day!")
        exit() 
        
    
#time.sleep(1)
speak("How can I help you?")
while 1:
    voice_data=record_audio()
    respond(voice_data)