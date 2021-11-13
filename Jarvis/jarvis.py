import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  

def wishMe(): 
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
         speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    else:
        speak("Good evening!")
    speak("Hello Akash, I am jarvis. How May I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")

    except Exception as e:
           #print(e)
           print("say that again plz...")  
           return "None" 
    return query     

if __name__ == "__main__": 
    wishMe()
    #while True: 
    if 1:
        query = takecommand().lower()

    #Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia..')
        query = query.replace("wikipedia","")
        results =wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open terasoft.tech' in query:
        webbrowser.open("terasoft.tech")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'H:\\Video\\punjabi'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0])) 

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,The time is now{strTime}")

    elif 'who are you' in query:
        speak(f"sir, i am jarvis")