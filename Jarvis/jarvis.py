import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Jarvis at your service. Please tell me how may I help you")

def recordAudio():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def search(query):
    query = " ".join(query.split())
    query = query.replace("wikipedia", "")
    url = f"https://en.wikipedia.org/wiki/{query}"
    webbrowser.open(url)
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

if __name__ == "__main__":
    wishMe()

    while True:
        query = recordAudio()
        query = query.lower()

        # Logic for executing tasks based on query

        # if 'wikipedia' in query:
        #     speak('Searching Wikipedia...')
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("According to Wikipedia")
        #     print(results)
        #     speak(results)

    if 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")

    elif 'open gmail' in query:
            webbrowser.open("gmail.com")

    elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

    elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

    elif 'search' in query:
            search(query)

    elif 'bye' in query:
            speak("Goodbye Sir, have a nice day")
            exit()