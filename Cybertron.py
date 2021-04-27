
import pyttsx3
import datetime
import speech_recognitionas as sr 

engine = pyttsx3 .init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id) 


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good Morning !")
    elif hour>+12 and hour<18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening")    

    speak("Hello  I am Cybertron , How May I help you")


def takeCommand():
    # It takes MicroPhone Input from the user and returns string output 
    r= sr.Recognizer(
        with sr.MicroPhone()as source:
            print('Listening...')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            quuery = r.recognise_google(audio, Language='en-in')
            print(f"User Said: {query}\n")  
        except Exception
        print(e)      
    )
if __name__ =="__main__":
    wishMe()
    takeCommand()