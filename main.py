import speech_recognition as sr #to recognize speech
import webbrowser #to search a link on web browser
import datetime
import time
import playsound #to play an audio file
import os #to remove created audio files
import random #to generate random names for audio file
from gtts import gTTS #Google text to speech
from time import ctime #get time details

r=sr.Recognizer() #speech_recognition object creation

def record_audio(ask=False):
    with sr.Microphone() as source: #setting physical microphone as a source
        if(ask):
            speak(ask)
        print("listening . . .")
        voice_data=""
        try:
            audio=r.listen(source,15,5) #listsening audio by r object ::listen(source,maximum time from start to first word listening ,time limit to listen whole command)
            voice_data=r.recognize_google(audio) #getting string obj 
            print(voice_data)
        except sr.WaitTimeoutError:
            speak("Wait time out error")
        except sr.UnknownValueError:
            speak("Sorry, I did not get that")
        except sr.RequestError:
            speak("Sorry, my speech server is down")
        return voice_data.lower()

def speak(audio_string):
    tts=gTTS(text=audio_string, lang="en") #creating audio file
    r = random.randint(1,1000000)
    audio_file="audio-"+str(r)+".mp3"
    tts.save(audio_file)   #saving audio file
    print(audio_string)
    playsound.playsound(audio_file) #playing audio file
    os.remove(audio_file)   #deleting to save memory

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True
    return False


def respond(voice_data):
    if "what" in voice_data:
        if there_exists(["name","you"]):
            speak("My name is Alexa")
            return
        if "time" in voice_data:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(time)
            return
    if there_exists(["search","find","google"]) :
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
    if there_exists(["exit","close","bye"]) :
        speak("Good Bye!")
        exit() 
        
    
#time.sleep(1)
speak("How can I help you?")
while 1:
    voice_data=record_audio()
    respond(voice_data)