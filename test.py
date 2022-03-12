import pyttsx3
import speech_recognition as sr
import windowsapps


engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand(event = " "):
      
     r=sr.Recognizer()
      
     with sr.Microphone() as source:
          
         r.pause_threshold=0.8
          
         r.energy_threshold=400

         print('listening..')
          
         r.non_speaking_duration=0.1
          
         audio=r.listen(source)
          

         try:
              
            
             print('recognizing..')
             audio = r.recognize_google(audio, language='en-in')
              
             query=audio.lower()         

             print(query)  
            
             return query
              
         except Exception as e:
             
               speak("Say that again please....")
            

def execute(appName):

            pass


while(True):
    pass



