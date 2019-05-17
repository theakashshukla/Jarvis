import pyttsx3




engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)