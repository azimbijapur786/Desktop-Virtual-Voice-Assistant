from asyncio.windows_events import NULL
from email.mime import image
from json.tool import main
from winreg import QueryInfoKey
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import windowsapps

from tkinter import *

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

window =Tk()

window.geometry("400x400")

window.title("Alex")

window.iconbitmap('robot.ico')

global var

var=StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Alex ")
    speak("Sir Please tell me how may I help you")

def takeCommand():
     #It takes mic input from user and returns string output
     r=sr.Recognizer()
     var.set("Listening...")
     window.update()
     with sr.Microphone() as source:
         r.pause_threshold=0.8
         r.energy_threshold=400
         r.adjust_for_ambient_noise(source,duration=1)
         audio=r.listen(source)

         try:
             audio = r.recognize_google(audio, language='en-in')
             query=audio.lower()
             

         except Exception as e:
            speak("Say that again please....")
            query=""

         if 'alex' in query:
            wishMe()
            var.set("")
         
         elif 'youtube' in query:
            speak("opening youtube ")
            webbrowser.open("youtube.com")
            var.set("")

         elif 'google' in query:
            speak("opening google ")
            webbrowser.open("google.com")
            var.set("")

         elif 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=2)
             speak("According to Wikipedia ")
             speak(results)
             var.set("")

         elif 'whatsapp' in query:
            speak("opening whatsapp ")
            webbrowser.open("https://web.whatsapp.com")
            var.set("")

         elif 'mail' in query:
            speak("opening gmail ")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            var.set("")

         elif 'classroom' in query:
            speak("opening google classroom ")
            webbrowser.open("https://classroom.google.com/h")
            var.set("")

         elif 'weather' in query:
            speak("showing weather news ")
            webbrowser.open("https://www.bing.com/search?q=weather&cvid=80b3646d80b745f3808c8e0549263256&aqs=edge.0.0l9.3156j0j1&pglt=43&FORM=ANSPA1&PC=EDGEDB")
            var.set("")

         elif'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            var.set("")

         elif 'code' in query:
            if windowsapps.find_app('Visual Studio Code')=="Application not found!":
               speak("You do not have this application")
            else:
               speak("opening Visual studio code ")
               windowsapps.open_app("Visual Studio Code")
            var.set("")

         elif 'word' in query:
            if windowsapps.find_app('Word')=="Application not found!":
               speak("You do not have this application")
            else:
               speak("opening word ")
               windowsapps.open_app("Word")
               var.set("")

         elif 'powerpoint' in query:
            if windowsapps.find_app('Powerpoint')=="Application not found!":
               speak("You do not have this application")
            else: 
               speak("opening power point")
               windowsapps.open_app("Powerpoint")
            var.set("")
         
         elif 'edge' in query:
            if windowsapps.find_app('Edge')=="Application not found!":
               speak("You do not have this application")
            else: 
               speak("opening Microsoft Edge")
               windowsapps.open_app("Edge")
            var.set("")
         
         elif 'chrome' in query:
            if windowsapps.find_app('chrome')=="Application not found!":
               speak("You do not have this application")
            else:
               windowsapps.open_app('chrome')
            var.set("")
         else:
            speak("I did not understand that")
            var.set("")

icons=PhotoImage(file="Images\power.png")

activate=Button(window,text="Speak",image=icons,command=takeCommand,height=70,width=70)

activate.place(x=160,y=200)

activate.config()

status=Label(window,text="Your Personal Voice Assistant",font='Forte 13',fg='white')

status.place(x=100,y=350)

status.config(bg="green")

ttl=Label(window,text="Alex",font='Forte 30',fg='white')

ttl.place(x=155,y=100)

ttl.config(bg='green')

lis=Label(window,textvariable=var)

lis.place(x=170,y=300)

window.mainloop() 






    