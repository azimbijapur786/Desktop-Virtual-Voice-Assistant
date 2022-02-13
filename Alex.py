from cgitb import text
from email.mime import image
from fileinput import filename
from json.tool import main
from multiprocessing.sharedctypes import Value
import tkinter
from winreg import QueryInfoKey
import Images
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import windowsapps
import random
import pyjokes
from tkinter import * 

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[0].id)

# Window Declaration Here
window =Tk()
window.geometry("400x600")
window.resizable(False,False)
window.title("Alex- Virtual Voice Assistant")

window.iconbitmap('robot.ico')

global var

var=StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning! Sir")

    elif hour>=12 and hour<17:
        speak("Good Afternoon! Sir")

    else:
        speak("Good Evening Sir!")
        window.update()
    speak("Allow me to introduce myself")
    window.update()
    speak("I am Alex, The virtual voice assistant ,and i'm here to assist you with variety of tasks, since the best i can, 24 hours a day 7 days a week, importing all preferences from herman to base")
    window.update()
    speak("Sir Please tell me how may I help you")
    window.update()
    
    
    
def tossAcoin():
    window.update()
    coins = [1,2]
    choice = random.choice(coins)
    window.update()
    if choice == 1:
        window.update()
        speak("Sir, its head")
    elif choice == 2:
        window.update()
        speak("Sir, its tails")
        window.update()
    window.update()
 
def rollAdice():
    dice = [1,2,3,4,5,6]
    value = random.choice(dice)
    if value == 1:
        speak("Sir, its 1 on dice")
    elif value == 2:
        speak("Sir, its 2 on dice ")
    elif value == 3:
        speak("Sir, its 3 on dice ")
    elif value == 4:
        speak("Sir, its 4 on dice ")
    elif value == 5:
        speak("Sir, its 5 on dice ")
    elif value == 6:
        speak("Sir, its 6 on dice ")       
        
def takeCommand(event = " "):
     #It takes mic input from user and returns string output
     window.update()
     r=sr.Recognizer()
     print("Listening...")
     var.set("Listening...")
     window.update()
     with sr.Microphone() as source:
         r.pause_threshold=0.8
         r.energy_threshold=400
         r.adjust_for_ambient_noise(source,duration=1)
         audio=r.listen(source)

         try:
             window.update()
             var.set("Recognizing...")
             print("Recognizing...")
             window.update()
             audio = r.recognize_google(audio, language='en-in')
             window.update()
             query=audio.lower()
             window.update()
             var.set("Speaking...")
             print(query)
             

         except Exception as e:
            window.update()
            speak("Say that again please....")
            window.update()
            query=""

         if 'who are you' in query:
            window.update()
            var.set("Speaking...")
            wishMe()
            window.update()
            var.set("")
         
         elif "toss a coin" in query:
            window.update()
            var.set("Speaking...")
            tossAcoin()
            window.update()
            var.set("")
         
         
         elif "roll a dice" in query:
                window.update()
                rollAdice()
                window.update()
                var.set("")
         
         elif 'youtube' in query:
            window.update()
            speak("opening youtube ")
            window.update()
            webbrowser.open("youtube.com")
            var.set("")
            window.update() 
            
         elif "joke" in query:
            window.update()
            speak(pyjokes.get_joke())
            window.update()
            var.set("")
            

         elif 'news' in query:
            window.update()
            speak("showing you some fresh news ")
            window.update()
            webbrowser.open("https://www.youtube.com/c/BBCNews")
            var.set("")

         elif 'drive' in query:
            window.update()
            speak("opening google drive ")
            window.update()
            webbrowser.open("https://drive.google.com/drive/my-drive")
            var.set("")

         elif 'meet' in query:
            window.update()
            speak("opening google meet ")
            window.update()
            webbrowser.open("https://meet.google.com/")
            var.set("")
         
         elif 'github' in query:
            window.update()
            speak("opening github ")
            window.update()
            webbrowser.open("https://github.com/")
            var.set("")

         elif 'google' in query:
            window.update()
            speak("opening google ")
            window.update()
            webbrowser.open("google.com")
            window.update()
            var.set("")

         elif 'wikipedia' in query:
             var.set("")
             window.update()
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query,sentences=2)
             window.update()
             speak("According to Wikipedia ")
             window.update()
             speak(results)
             window.update()

         elif 'whatsapp' in query:
            window.update()
            speak("opening whatsapp ")
            window.update()
            webbrowser.open("https://web.whatsapp.com")
            window.update()
            var.set("")

         elif 'mail' in query:
            window.update()
            speak("opening gmail ")
            window.update()
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            window.update()
            var.set("")

         elif 'classroom' in query:
            window.update()
            speak("opening google classroom ")
            window.update()
            webbrowser.open("https://classroom.google.com/h")
            window.update()
            var.set("")

         elif 'weather' in query:
            window.update()
            speak("showing weather news ")
            window.update()
            webbrowser.open("https://www.bing.com/search?q=weather&cvid=80b3646d80b745f3808c8e0549263256&aqs=edge.0.0l9.3156j0j1&pglt=43&FORM=ANSPA1&PC=EDGEDB")
            window.update()
            var.set("")

         elif 'time' in query:
            window.update()
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
            window.update()
            var.set("")

         elif 'code' in query:
            if windowsapps.find_app('Visual Studio Code')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               speak("opening Visual studio code ")
               window.update()
               windowsapps.open_app("Visual Studio Code")
               window.update()
            var.set("")

         elif 'word' in query:
            if windowsapps.find_app('Word')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               speak("opening word ")
               window.update()
               windowsapps.open_app("Word")
               window.update()
               var.set("")

         elif 'powerpoint' in query:
            window.update()
            if windowsapps.find_app('Powerpoint')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else: 
               window.update()
               speak("opening power point")
               window.update()
               windowsapps.open_app("Powerpoint")
               window.update()
            var.set("")
         
         elif 'edge' in query:
            if windowsapps.find_app('Edge')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else: 
               window.update()
               speak("opening Microsoft Edge")
               window.update()
               windowsapps.open_app("Edge")
               window.update()
            var.set("")
         
         elif 'chrome' in query:
            window.update()
            if windowsapps.find_app('chrome')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('chrome')
               window.update()
               speak("Opening google chrome")
               window.update()
            var.set("")
         
         elif 'calculator' in query:
            window.update()
            if windowsapps.find_app('calculator')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('calculator')
               window.update()
               speak("Opening calculator")
               window.update()
            var.set("")

         elif 'camera' in query:
            window.update()
            if windowsapps.find_app('camera')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('camera')
               window.update()
               speak("Opening camera")
               window.update()
            var.set("")

         elif 'zoom' in query:
            window.update()
            if windowsapps.find_app('zoom')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('zoom')
               window.update()
               speak("Opening zoom")
               window.update()
            var.set("")

         elif 'teams' in query:
            window.update()
            if windowsapps.find_app('microsoft teams')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('microsoft teams')
               window.update()
               speak("Opening microsoft teams")
               window.update()
            var.set("")

         elif 'firefox' in query:
            window.update()
            if windowsapps.find_app('firefox')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('firefox')
               window.update()
               speak("Opening firefox")
               window.update()
            var.set("")
      
         elif 'eclipse' in query:
            window.update()
            if windowsapps.find_app('eclipse')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('eclipse')
               window.update()
               speak("Opening eclipse")
               window.update()
            var.set("")

         elif 'intellij' in query:
            window.update()
            if windowsapps.find_app('intellij idea')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('intellij idea')
               window.update()
               speak("Opening intellij idea")
               window.update()
            var.set("")

         elif 'paint' in query:
            window.update()
            if windowsapps.find_app('paint')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('paint')
               window.update()
               speak("Opening paint")
               window.update()
            var.set("")

         elif 'notepad' in query:
            window.update()
            if windowsapps.find_app('notepad')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('notepad')
               window.update()
               speak("Opening notepad")
               window.update()
            var.set("")

         elif 'excel' in query:
            window.update()
            if windowsapps.find_app('excel')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('excel')
               window.update()
               window.update()
               speak("Opening excel")
               window.update()
            var.set("")

         elif 'pictures' in query:
            window.update()
            if windowsapps.find_app('photos')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('photos')
               window.update()
               window.update()
               speak("Opening photos")
               window.update()
            var.set("")

         elif 'settings' in query:
            window.update()
            if windowsapps.find_app('control panel')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('control panel')
               window.update()
               window.update()
               speak("Opening control panel")
               window.update()
            var.set("")

         elif 'photoshop' in query:
            window.update()
            if windowsapps.find_app('adobe photoshop')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('adobe photoshop')
               window.update()
               window.update()
               speak("Opening adobe photoshop")
               window.update()
            var.set("")
            
         elif "made you":
                window.update()
                speak("I was born when many bright minds")
                window.update()
                speak("like Azim ,Rohan ,Arkaan ,Abuzar")
                window.update()
                speak("came together to create an assistant, just for you")
                window.update()
                var.set("")
         elif 'instagram' in query:
            window.update()
            if windowsapps.find_app('instagram')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('instagram')
               window.update()
               window.update()
               speak("Opening instagram")
               window.update()
            var.set("")

         elif 'one note' in query:
            window.update()
            if windowsapps.find_app('onenote')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('onenote')
               window.update()
               window.update()
               speak("Opening onenote")
               window.update()
            var.set("")

         elif 'to do' in query:
            window.update()
            if windowsapps.find_app('to do')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('to do')
               window.update()
               window.update()
               speak("Opening microsoft to do")
               window.update()
            var.set("")

         elif 'your phone' in query:
            window.update()
            if windowsapps.find_app('your phone')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('your phone')
               window.update()
               window.update()
               speak("Opening your phone")
               window.update()
            var.set("")

         elif 'telegram' in query:
            window.update()
            if windowsapps.find_app('telegram')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('telegram')
               window.update()
               window.update()
               speak("Opening telegram")
               window.update()
            var.set("")
            
         elif "my name" in query:
                speak("Of course! You said your name is arkaan. You are wonderful human being, and I am your assistant")
         elif 'powershell' in query:
            window.update()
            if windowsapps.find_app('powershell')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('powershell')
               window.update()
               window.update()
               speak("Opening windows powershell")
               window.update()
            var.set("")

         elif 'bash' in query:
            window.update()
            if windowsapps.find_app('git bash')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('git bash')
               window.update()
               window.update()
               speak("Opening git bash")
               window.update()
            var.set("")

         elif 'python' in query:
            window.update()
            if windowsapps.find_app('IDLE (Python 3.10 64-bit)')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('IDLE (Python 3.10 64-bit)')
               window.update()
               window.update()
               speak("Opening python shell")
               window.update()
            var.set("")

         elif 'calendar' in query:
            window.update()
            if windowsapps.find_app('calendar')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('calendar')
               window.update()
               window.update()
               speak("Opening calendar")
               window.update()
            var.set("")

         elif 'xbox' in query:
            window.update()
            if windowsapps.find_app('xbox game bar')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('xbox game bar')
               window.update()
               window.update()
               speak("Opening xbox game bar")
               window.update()
            var.set("")

         elif 'android studio' in query:
            window.update()
            if windowsapps.find_app('android studio')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('android studio')
               window.update()
               window.update()
               speak("Opening android studio")
               window.update()
            var.set("")

         elif 'filmora' in query:
            window.update()
            if windowsapps.find_app('filmora')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('filmora')
               window.update()
               window.update()
               speak("Opening filmora")
               window.update()
            var.set("")

         elif "thank you" in query:
                window.update()
                speak("It is pleasure to help")
                var.set("")
         elif "sleep" in query:
                window.update()
                speak("Ok sir, as your wish")
                var.set("")
                exit()
         elif "good night" in query:
                window.update()
                speak("Good Night Sir, Sweet Dreams")
                exit()
         elif 'premiere' in query:
            window.update()
            if windowsapps.find_app('adobe premiere pro')=="Application not found!":
               window.update()
               speak("You do not have this application")
               window.update()
            else:
               window.update()
               windowsapps.open_app('adobe premiere pro')
               window.update()
               window.update()
               speak("Opening adobe premiere pro")
               window.update()
            var.set("")

         else:
             window.update()
             speak("I did not understand that")
             var.set("")

def show_info(event = " "):
       global info
       info = Toplevel(window)
       info.title("Information")
       info.geometry("250x250")
       info.resizable(False,False)
       info_info = "Alex is made by\nAZIM \nROHAN \nARKAAN \nABUZAR"
       info_label = Label(info, text = info_info)
       info_label.pack(anchor= "n")
       ok_button = Button(info, command = info.destroy, text = "OK").pack(anchor="s", side = BOTTOM)

#Opens window on click ? button  
def show_help(event = " "):
       global help 
       help = Toplevel(window)
       help.title("Help")
       help.geometry("270x250")
       help.resizable(False,False)
       help_info = "1. Click on power button to start\n 2. Use Ctrl+m to acces power button"
       help_label = Label(help, text = help_info,font = ("ALGERIAN", 10, BOLD))
       help_label.pack(anchor = "n")
       ok_button = Button(help, command = help.destroy, text = "OK", pady = 10).pack(anchor="s", side = BOTTOM)
      
      
# WIDGETS HERE
#Background Image
bg_image = PhotoImage(file = "Images\\background.png")
bg_label = Label(window, image = bg_image).pack()
icons=PhotoImage(file="Images\power.png")
activate=Button(window,text="Speak",command=takeCommand,relief=FLAT,image=icons,height=70,width=70)
window.bind('<Control-m>',takeCommand)

#activate=Button(window,text="Speak",command=takeCommand,relief=FLAT,image=icons,height=70,width=70)


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


#About Button
about_image = PhotoImage(file = "Images\info.png")
about_button = Button(window,image = about_image,relief=FLAT, command = show_info)
about_button.pack(anchor= "ne")
window.bind('<Control-i>',show_info)
#Help Button
help_image = PhotoImage(file = "Images\help.png")
help_button = Button(window, image = help_image,relief=FLAT, command= show_help)
help_button.pack(anchor= "ne")
window.bind('<Control-h>',show_help)

window.mainloop() 
   