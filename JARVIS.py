import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour <12:
        speak("Good morning")
    elif hour>=12 and hour<13:
        speak("Good afteroon")
    else:
        speak("Good evening")

    speak("I am JARVIS, your assistant. How may I help you?")

def takeCommand():
    recognise = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognise.pause_threshold = 1
        audio = recognise.listen(source)

    try:
        print("Recognizing...")
        query = recognise.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:

        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
             webbrowser.open("youtube.com")
             speak("Opening youtube")
        
        elif 'open wordpress' in query:
            webbrowser.open("https://wordpress.com")
            speak("Opening Wordpress")
        
        elif 'open github' in query:
            webbrowser.open("https://github.com")
            speak("Opening Github")

        elif 'thank you' in query:
            speak("exiting...")
            exit() 
        
        

            
        


