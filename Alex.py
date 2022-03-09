import threading
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import windowsapps
import random
import psutil
import speedtest
import wolframalpha
import wikipedia
import time
import os
from tkinter import * 


global var
global varBat

#Text to speech 

engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)

#Main Window Initialization

window =Tk()
window.resizable(False,False)
window.title("Alex- Virtual Voice Assistant")
window.iconbitmap('robot.ico')
window.geometry("400x600+550+100")
window.config(bg='yellow')

#For Label Text

var=StringVar()
varBat=StringVar()

#Making it speak

def speak(audio):
    engine.say(audio)
    try:
      engine.runAndWait()
    except Exception as e:
       print("nothing much")

# Battery Status
try:

   battery = psutil.sensors_battery()
   percent = battery.percent

   if (percent<20):
      varBat.set("Battery Low !! "+str(percent)+"%")

   else:
      varBat.set("Battery percent: "+str(percent)+"%")

except Exception as f:
   varBat.set("")

#Some Trivial commands

    
def tossAcoin():
     
    coins = [1,2]
    choice = random.choice(coins)
     
    if choice == 1:
         
        speak("Sir, its head")
    elif choice == 2:
         
        speak("Sir, its tails")
         
     
 
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

#Taking user input
        
def takeCommand(event = " "):
      
     var.set("....")
      
     r=sr.Recognizer()
      
     with sr.Microphone() as source:
          
         r.pause_threshold=0.8
          
         r.energy_threshold=400
          
         r.non_speaking_duration=0.1
          
         audio=r.listen(source)
          

         try:
              
             var.set(".....")
              
             audio = r.recognize_google(audio, language='en-in')
              
             query=audio.lower()         

             print(query)  
              
         except Exception as e:
             
            speak("Say that again please....")
             
            query=""

         if "toss a coin" in query:
             
            tossAcoin()
             
            var.set("")
         
         
         elif "roll a dice" in query:
             
            rollAdice()
             
            var.set("")
            
         
         elif "thank you" in query:
             
            speak("Always my pleasure")
             
            exit()

 #Web based commands

         elif 'youtube' in query:
             
            speak("opening youtube ")
             
            webbrowser.open("youtube.com")

            var.set("")
         
         elif 'ask' in query:
            speak('Always here to answer your questions,give me a second')
            client = wolframalpha.Client('GRL2AR-KL6GUV7K2R')
            question=query.replace("I want to ask","")
            res = client.query(question)
            try:
               answer = next(res.results).text
               speak(answer)
            except Exception as e:
               speak("I did not understand that question")
            var.set("")
              

         elif 'news' in query:
             
            speak("showing you some fresh news ")
             
            webbrowser.open("https://www.youtube.com/c/BBCNews")

            var.set("")

         elif 'drive' in query:
             
            speak("opening google drive ")
             
            webbrowser.open("https://drive.google.com/drive/my-drive")

            var.set("")

         elif 'meet' in query:
             
            speak("opening google meet ")
             
            webbrowser.open("https://meet.google.com/")

            var.set("")
         
         elif 'github' in query:
             
            speak("opening github ")
             
            webbrowser.open("https://github.com/")

            var.set("")


         elif 'whatsapp' in query:
             
            speak("opening whatsapp , please wait")
             
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
         
         if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query =query.replace("wikipedia", "")
            try:
               results = wikipedia.summary(query, sentences=2)
               speak("According to Wikipedia")
               speak(results)
            except Exception as e:
               speak("I did not understand what to search for")
            var.set("")

#Time command

         elif 'time' in query:
             
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
             
            var.set("")

#Internet speed test        

         elif 'internet speed' in query:
            speak("Please wait")
             
            st = speedtest.Speedtest()
             
            speak("Checking download speed")
             
            speak("Your download speed is"+str(int(st.download()/10**6))+"Megabits per second")
             
            speak("Checking upload speed")
             
            speak("Your upload speed is"+str(int(st.upload()/10**6))+"Megabits per second")
             
            var.set("")
         
#System commands

         elif 'code' in query:
            if windowsapps.find_app('Visual Studio Code')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               speak("opening Visual studio code , please wait")
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
               speak("Opening google chrome")
                
            var.set("")
         
         elif 'calculator' in query:
             
            if windowsapps.find_app('calculator')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('calculator')
               speak("Opening calculator")
                
            var.set("")

         elif 'camera' in query:
             
            if windowsapps.find_app('camera')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('camera')
               speak("Opening camera")
                
            var.set("")

         elif 'zoom' in query:
             
            if windowsapps.find_app('zoom')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('zoom')
               speak("Opening zoom")
                
            var.set("")

         elif 'teams' in query:
             
            if windowsapps.find_app('microsoft teams')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('microsoft teams')
               speak("Opening microsoft teams")
                
            var.set("")

         elif 'firefox' in query:
             
            if windowsapps.find_app('firefox')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('firefox')
               speak("Opening firefox")
                
            var.set("")
      
         elif 'remember that' in query:
            
            remeberMsg = query.replace("remember that ","")
            remeberMsg = remeberMsg.replace("alex","")
            speak("okay I will remember that :"+remeberMsg)
            remeber = open('memory.txt','w')
            remeber.write(remeberMsg)
            remeber.close()
            var.set("")


         elif 'what do you remember' in query:
            remeber = open('memory.txt','r')
            speak("You told me that:" + remeber.read())
            var.set("")


         elif 'eclipse' in query:
             
            if windowsapps.find_app('eclipse')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('eclipse')
               speak("Opening eclipse")
                
            var.set("")

         elif 'intellij' in query:
             
            if windowsapps.find_app('intellij idea')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('intellij idea')
               speak("Opening intellij idea")
                
            var.set("")

         elif 'paint' in query:
             
            if windowsapps.find_app('paint')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('paint')
               speak("Opening paint")
                
            var.set("")

         elif 'notepad' in query:
             
            if windowsapps.find_app('notepad')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('notepad')
               speak("Opening notepad")
                
            var.set("")

         elif 'excel' in query:
             
            if windowsapps.find_app('excel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('excel')
               speak("Opening excel")
                
            var.set("")

         elif 'picture' in query:
             
            if windowsapps.find_app('photos')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('photos')
               speak("Opening photos")
                
            var.set("")

         elif 'settings' in query:
             
            if windowsapps.find_app('control panel')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('control panel')
               speak("Opening control panel")
                
            var.set("")

         elif 'play music' in query:
             
            speak("Opening media player")
            windowsapps.open_app("windows media player")
            var.set(" ")

         elif 'photoshop' in query:
             
            if windowsapps.find_app('adobe photoshop')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('adobe photoshop')
               speak("Opening adobe photoshop")
                
            var.set("")

         elif 'instagram' in query:
             
            if windowsapps.find_app('instagram')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('instagram')
               speak("Opening instagram") 
            var.set("")

         elif 'one note' in query:
             
            if windowsapps.find_app('onenote')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('onenote') 
               speak("Opening onenote")  
            var.set("")

         elif 'to do' in query:
             
            if windowsapps.find_app('to do')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('to do')
               speak("Opening microsoft to do")
            var.set("")

         elif 'your phone' in query:
             
            if windowsapps.find_app('your phone')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('your phone')
               speak("Opening your phone")
                
            var.set("")

         elif 'telegram' in query:
             
            if windowsapps.find_app('telegram')=="Application not found!": 
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('telegram')
               speak("Opening telegram")
            var.set("")
   
         elif 'powershell' in query:
             
            if windowsapps.find_app('powershell')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('powershell')
               speak("Opening windows powershell") 
            var.set("")

         elif 'bash' in query:
             
            if windowsapps.find_app('git bash')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('git bash')
               speak("Opening git bash")
            var.set("")

         elif 'python' in query:
            if windowsapps.find_app('IDLE (Python 3.10 64-bit)')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('IDLE (Python 3.10 64-bit)')    
               speak("Opening python shell")
            var.set("")

         elif 'calendar' in query:
            if windowsapps.find_app('calendar')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('calendar')
               speak("Opening calendar")
            var.set("")

         elif 'xbox' in query:
            if(windowsapps.find_app('xbox game bar')=="Application not found!"):  
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('xbox game bar')               
               speak("Opening xbox game bar")              
            var.set("")

         elif 'android studio' in query:
            if windowsapps.find_app('android studio')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('android studio')
               speak("Opening android studio")
                
            var.set("")

         elif 'filmora' in query:
             
            if windowsapps.find_app('filmora')=="Application not found!":
               speak("You do not have this application")
                
            else:
                
               windowsapps.open_app('filmora')
               speak("Opening filmora")
            var.set("")

         elif 'premiere' in query:
             
            if windowsapps.find_app('adobe premiere pro')=="Application not found!":
               speak("You do not have this application")
                
            else:
               windowsapps.open_app('adobe premiere pro')
               speak("Opening adobe premiere pro")
                
               
            var.set("")
         
         elif 'power of' in query:
            speak("Logging of the computer in 5 seconds")
            time.sleep(5)
            os.system("shutdown /s /t 1")

         else:
              
             speak("I did not understand that")
              
             var.set("")
         
#Function for About and Back button

imgBackButton=PhotoImage(file="Images\\back2.png")

def goBack(event=" "):
       info.destroy()
       window.deiconify()

def show_info(event = " "):

       global info
       info = Toplevel(window)
       info.title("About")
       info.geometry("400x600+550+100")
       info.config(bg='yellow')
       info.resizable(False,False)
       window.withdraw()
       back_button = Button(info, command =goBack,relief=FLAT,image=imgBackButton,bg='yellow')
       back_button.pack(anchor ="nw", side = TOP)
       info_info = "\n\n\n\nAlex is your personalized desktop\n assistant which assists you in your \n daily computing tasks thereby increasing\n efficiency at work\n\n It is developed by Computer Engineering \n Students of M.H.Saboo Siddik College\n of Engineering,Mumbai:\n\n Rohan Bhabhal\nAzim Ahmed Bijapur\nArkaan Khan\nAbuzar Shaikh\n\nUnder the guidance of :\nProf.Anand Bali,\nAssistant Professor,Mhssce"
       info_label = Label(info, text = info_info,bg='yellow')
       titleLabel= Label(info,text='About Us',bg='yellow',font='Calibri 25')
       titleLabel.place(x=140,y=20)
       info_label.config(font='Calibri 14')
       info_label.pack(anchor= "n")
       info.iconbitmap('robot.ico')

# Thread

def start_cmd():
   t2=threading.Thread(target=takeCommand)
   t2.start()
      
# Gui functionality

icons=PhotoImage(file="Images\\mic.png")

activate=Button(window,text="Speak",command=start_cmd ,relief=FLAT,image=icons,height=70,width=70,anchor=CENTER,border=5,borderwidth=5,bg='yellow')

activate.place(x=160,y=230)

status=Label(window,text="Your Personal Voice Assistant",font='Forte 15',bg='yellow')

status.place(x=67,y=450)

ttl=Label(window,text="Alex",font='Forte 50',anchor=CENTER,bg='yellow')

ttl.place(x=127,y=100)

lis=Label(window,textvariable=var,padx=12,pady=5,anchor=CENTER,font='Forte 40',bg='yellow')

lis.place(x=158,y=330)

batteryStatus=Label(window,textvariable=varBat,font="Aparajita 16",bg='yellow')

batteryStatus.place(x=11,y=9)

about_image = PhotoImage(file = "Images\info2.png")

about_button = Button(window,image = about_image,relief=FLAT, command = show_info,bg='yellow')

about_button.pack(anchor="ne")

window.bind('<Control-i>',show_info)

window.mainloop()