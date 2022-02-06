import pyttsx3
import pyaudio
import speech_recognition

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('python I D L E')