from random import randint
from signal import signal
import pyttsx3
import random
import datetime
from regex import P
import speech_recognition as sr
import webbrowser
import windowsapps
import wolframalpha
import time
from PIL import ImageGrab
import psutil
import os
import screen_brightness_control
import threading
import keyboard
from tkinter import *

global varbBat

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

engine.setProperty('rate',200)

def Gui():
   window =Tk()
   window.resizable(False,False)
   window.title("Alex- Virtual Voice Assistant")
   window.iconbitmap('robot.ico')
   window.geometry("400x500+550+100")
   window.config(bg='yellow')
   ttl=Label(window,text="Alex",font='Forte 50',anchor=CENTER,bg='yellow')
   ttl.place(x=127,y=60)
   status=Label(window,text="*Your Personal Voice Assistant*",font='Forte 15',bg='yellow')
   status.place(x=67,y=380)
   varbBat=StringVar()
   about_image = PhotoImage(file = "nanotechnology.png")
   try:
      battery = psutil.sensors_battery()
      percent = battery.percent
      if (percent<20):
         varbBat.set("Battery Low !! "+str(percent)+"%")

      else:
         varbBat.set("Battery percent: "+str(percent)+"%")
   except Exception as f:
         varbBat.set("")
   batteryStatus=Label(window,textvariable=varbBat,font="Aparajita 16",bg='yellow')
   batteryStatus.place(x=11,y=9)
   lis=Label(window,image=about_image,padx=12,pady=5,anchor=CENTER,font='Forte 40',bg='yellow')
   lis.place(x=135,y=200)
   window.mainloop()
   
def kill_process(PROCNAME):
  for proc in psutil.process_iter():
    try:
      if proc.name().lower() == PROCNAME.lower():
        proc.kill()
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      return False

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alex Sir. Please tell me how may I help you") 

def speak(audio):
    engine.say(audio)
    try:
      engine.runAndWait()
    except Exception as e:
       print("nothing much")



def takeCommand(event = " "):

     print("Listening...\n")
      
     r=sr.Recognizer()
 
     with sr.Microphone() as source:
          
         r.pause_threshold=0.8
          
         r.energy_threshold=300
          
         r.non_speaking_duration=0.1

         r.adjust_for_ambient_noise(source,0.2)

         print("Recognizing...\n")

         audio=r.listen(source)

         try:

             audio = r.recognize_google(audio, language='en-in')
              
             query=audio.lower()         

             print(query+"\n")  
              
         except Exception as e:
             
               query=""

         if 'type' in query:
            sentence=query.replace('type','')
            keyboard.write(sentence)

         elif 'youtube' in query:
             
            speak("opening youtube ")
             
            webbrowser.open("youtube.com")


         elif 'tell me' in query:
            speak('Always here to answer your questions,give me a second')
            client = wolframalpha.Client('GRL2AR-KL6GUV7K2R')
            question=query.replace("tell me","")
            print(question)
            res = client.query(question)
            try:
               answer = next(res.results).text
               speak(answer)
            except Exception as e:
               speak("I did not understand that question")
             
              

         elif 'news' in query:
             
            speak("showing you some fresh news ")
             
            webbrowser.open("https://www.youtube.com/c/BBCNews")

             

         elif 'drive' in query:
             
            speak("opening google drive ")
             
            webbrowser.open("https://drive.google.com/drive/my-drive")

             

         elif 'meet' in query:
             
            speak("opening google meet ")
             
            webbrowser.open("https://meet.google.com/")

         
         elif 'xbox' in query:
            if(windowsapps.find_app('xbox game bar')=="Application not found!"):  
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('xbox game bar')               
               speak("Opening xbox game bar")              
             

         elif 'game' in query:
             
            speak("As you wish ")
             
            webbrowser.open("https://chromedino.com/")

             
         
         elif 'github' in query:
             
            speak("opening github ")
             
            webbrowser.open("https://github.com/")
         

         elif 'whatsapp' in query:
             
            speak("opening whatsapp , please wait")
             
            webbrowser.open("https://web.whatsapp.com")
             
             

         elif 'mail' in query:
             
            speak("opening gmail ")
             
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

         elif 'fiddle' in query:
             
            speak("opening sql fiddle ")
             
            webbrowser.open("https://www.db-fiddle.com/f/6GJsV5KP3csKy9vg4y2us7/0")
             
             

         elif 'classroom' in query:
             
            speak("opening google classroom ")
             
            webbrowser.open("https://classroom.google.com/h")
             
             

         elif 'weather' in query:
             
            speak("showing weather news ")

            webbrowser.open("https://www.bing.com/search?q=weather&cvid=80b3646d80b745f3808c8e0549263256&aqs=edge.0.0l9.3156j0j1&pglt=43&FORM=ANSPA1&PC=EDGEDB")

             
         

#Time command

         elif 'time' in query:
             
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
             
             

#Internet speed test        

         elif 'internet speed' in query:
            
            speak("checking internet speed")

            webbrowser.open("https://www.speedtest.net/")

             
         
#System commands

         elif 'code' in query:
            if windowsapps.find_app('Visual Studio Code')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               speak("opening Visual studio code , please wait")
               windowsapps.open_app("Visual Studio Code")

         elif 'increase brightness' in query:
            current=screen_brightness_control.get_brightness()
            screen_brightness_control.set_brightness(current+10)
            if current==100:
               speak("Maximum brightness")
            else:
               speak("Increased")

         elif 'reduce brightness' in query:
            current=screen_brightness_control.get_brightness()
            screen_brightness_control.set_brightness(current-10)
            if current==0:
               speak("Minimum brightness")
            else:
               speak("Decreased")


         elif 'word' in query:
            if windowsapps.find_app('Word')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               speak("opening word ")
               windowsapps.open_app("Word")
         
         elif 'screenshot' in query:

            image = ImageGrab.grab(all_screens=True)
            i=random.randint(0,1000)
            image.save(f'sc{i}.png')    
            speak("Taken")

         elif 'powerpoint' in query:
             
            if windowsapps.find_app('Powerpoint')=="Application not found!":
               speak("You do not have this application")
                
            else: 
                
               speak("opening power point")
               windowsapps.open_app("Powerpoint")
                
             
         
         elif 'edge' in query:
            if windowsapps.find_app('Edge')=="Application not found!":
               speak("You do not have this application")
                
            else: 
                
               speak("opening Microsoft Edge")
               windowsapps.open_app("Edge")
                
             
         
         elif 'chrome' in query:
             
            if windowsapps.find_app('chrome')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('chrome')
               speak("Opening google chrome")
                
             
         
         elif 'calculator' in query:
             
            if windowsapps.find_app('calculator')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('calculator')
               speak("Opening calculator")
                
             

         elif 'camera' in query:
             
            if windowsapps.find_app('camera')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('camera')
               speak("Opening camera")
                
             

         elif 'zoom' in query:
             
            if windowsapps.find_app('zoom')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('zoom')
               speak("Opening zoom")
                
             

         elif 'firefox' in query:
             
            if windowsapps.find_app('firefox')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('firefox')
               speak("Opening firefox")
                
             
         
         # Take some notes
      
         elif 'remember that' in query:
            
            qa=query
            remeberMsg = qa.replace("remember that ","")
            speak("okay I will remember that :")
            remeber = open('memory.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
             


         elif 'what do you remember' in query:
            remeber = open('memory.txt','r')
            speak("You told me that:" + remeber.read())
            remeber.close()
             

         # System commands

         elif 'eclipse' in query:
             
            if windowsapps.find_app('eclipse')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('eclipse')
               speak("Opening eclipse")
                
             

         elif 'intellij' in query:
             
            if windowsapps.find_app('intellij idea')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('intellij idea')
               speak("Opening intellij idea")
                
             

         elif 'paint' in query:
             
            if windowsapps.find_app('paint')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('paint')
               speak("Opening paint")
                
             

         elif 'notepad' in query:
             
            if windowsapps.find_app('notepad')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('notepad')
               speak("Opening notepad")
                
             

         elif 'excel' in query:
             
            if windowsapps.find_app('excel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('excel')
               speak("Opening excel")
                
             

         elif 'picture' in query:
             
            if windowsapps.find_app('photos')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('photos')
               speak("Opening photos")
                
             

         elif 'control panel' in query:
             
            if windowsapps.find_app('control panel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('control panel')
               speak("Opening control panel")
                
             

         elif 'play music' in query:
             
            speak("Opening media player")
            windowsapps.open_app("windows media player")

         elif 'photoshop' in query:
             
            if windowsapps.find_app('adobe photoshop')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('adobe photoshop')
               speak("Opening adobe photoshop")
                
             


         elif 'to do' in query:
             
            if windowsapps.find_app('to do')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('to do')
               speak("Opening microsoft to do")
             

         elif 'your phone' in query:
             
            if windowsapps.find_app('your phone')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('your phone')
               speak("Opening your phone")
                
             
   
         elif 'powershell' in query:
             
            if windowsapps.find_app('powershell')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('powershell')
               speak("Opening windows powershell") 
             

         elif 'bash' in query:
             
            if windowsapps.find_app('git bash')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('git bash')
               speak("Opening git bash")
             

         elif 'python' in query:
            if windowsapps.find_app('IDLE (Python 3.10 64-bit)')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('IDLE (Python 3.10 64-bit)')    
               speak("Opening python shell")
             

         elif 'calendar' in query:
            if windowsapps.find_app('calendar')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('calendar')
               speak("Opening calendar")
             

         elif 'android studio' in query:
            if windowsapps.find_app('android studio')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('android studio')
               speak("Opening android studio")
                
             

         # Video Editting software

         elif 'filmora' in query:
             
            if windowsapps.find_app('filmora')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('filmora')
               speak("Opening filmora")
             

         elif 'premiere' in query:
             
            if windowsapps.find_app('adobe premiere pro')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('adobe premiere pro')
               speak("Opening adobe premiere pro")
             
         
         elif 'power of' in query:
            speak("Logging of the computer in 5 seconds")
            time.sleep(5)
            os.system("shutdown /s /t 1")

         elif 'sleep' in query:
            speak("As you wish")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

         elif 'restart' in query:
            speak("As you wish")
            os.system("shutdown /r /t 0")
         

#Else
            
         elif 'quit' in query:
             speak("Have a nice day")
             exit()
         
         else:
            query=""
            speak("")


def start_cmd():
      t2=threading.Thread(target=Gui)
      t2.start()

start_cmd()
while(True):
       
        wishMe()
        
        while(True):
        
            takeCommand()
    
     

