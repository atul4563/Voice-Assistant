import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
from pyjokes import *
import webbrowser
import os
import requests
import newsapi

NEWS_API_KEY = "a2eaea25636849db9be30f88bed15952"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/top-headlines"
NEWS_API_PARAMS = {
    "country" : "india",
    "apiKey" : NEWS_API_KEY,
}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_news():
    response = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMS)
    news_data = response.json()
    if response.status_code == 200:
        articles = news_data.get("articles", [])
        return articles
    # else:
        # print(f"Error {response.status_code}: {news_data.get("message", "Unknown error")}")
        # return None
    
def speak_news():
    articles = get_news()
    if articles:
        for index, article in enumerate(articles, start=1):
            title = article["title"]
            source = article["source"]["name"]
            print(f"{index}. {title} from {source}")
            engine.say(f"News {index}: {title} from {source}")
        engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!") 

    speak("I am Nova sir, Please tell me how may I help you")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
    except Exception as e :
        print("Say that again please...")
        return "None"
    return query


if __name__=="__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        
        # Logic for  executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")    
            
        elif 'open college website' in query:
            webbrowser.open("rmlau.ac.in")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'jokes' in query:
            speak("Get ready for some chuckles")
            joke =pyjokes.get_joke()
            speak(joke) 
            print(joke)   

        elif 'open code' in query: 
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'news' in query:
            speak("Sure Sir, I will read news for you")
            speak_news()
        