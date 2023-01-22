# Vistual Assitant: Nock.AI
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return ""

speak("Hello, Welcome to the Nock AI. How can I help you?")
while True:
    text = listen()
    if text.lower() == "exit":
        speak("Goodbye!")
        break
    elif "time" in text.lower():
        import datetime
        now = datetime.datetime.now()
        speak("The current time is " + now.strftime("%H:%M:%S"))
    else:
        speak("I'm sorry, I didn't understand what you said. Could you please repeat that?")