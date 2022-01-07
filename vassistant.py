import datetime
import os
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install SpeechRecognition
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
from time import sleep
import random
import smtplib
import requests
import pyautogui as pg
# import pywhatkit as kit


engine = pyttsx3.init()  # initialise pyttsx3
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0-2 range for different voices
voicespeed = 140  # setting speed
engine.setProperty('rate', voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sleep(2)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=2,phrase_time_limit=5)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "---"
    return query

def whatsapp():
    try:
        speak("whom should i send the message")
        contact=takeCommand().lower()
        speak(" what do you want to say?")
        msg=takeCommand().lower()
        wb.open('https://web.whatsapp.com/')

        pg.sleep(15)
        print(pg.position())
        # click on search bar
        pg.click(187,255)
        speak("searching person")
        pg.typewrite(contact)
        pg.sleep(10)
        # #click on person 
        pg.click(163,319)
        pg.sleep(10)
        pg.click(763,966)
        speak("writing msg")
        pg.typewrite(msg)
        pg.sleep(10)
        pg.click(1790,965) 
        # speak("pls tell time in hour")
        # hr=takeCommand().lower()
        # speak("pls tell time in minute")
        # m=takeCommand().lower()
        # kit.sendwhatmsg("+919766176749","jbsjbdjsbj",19,19)
        speak("msg sent")
    except Exception as e:
        print(e)


def time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ssasane451@gmail.com', 'ur password')
    server.sendmail('ssasane451@gmail.com', to, content)
    server.close()

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is")
    print(day, month, year)
    speak(day)
    speak(month)
    speak(year)

def geo():
    ipadd=requests.get('https://api.ipify.org').text
    speak(ipadd)

def wishme():
    speak("Welcome back sir")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good evening")
    else:
        speak("good night")
    speak("I am Jarvis Sir. Please tell me how may I help you") 


# Open chrome/website
def open_chrome():
    url = "https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)


if __name__ == "__main__":

    wishme()

    try:

        while True:
            query = takeCommand().lower()
            print(query)

            if "your name"in query:
                speak(" Im chargo your assistant . iam designed to do simple tasks to help you out.")
                
            elif "time" in query:
                time()

            elif "date" in query:
                date()

            # open chrome
            elif "open google" in query:
                open_chrome()

            # Wikipedia search
            elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)

            # Chrome search
            elif "search" in query:
                speak("what should i search on google")  
                searchg=takeCommand().lower()
                speak("opening google")
                speak("searching..")
                wb.open('https://www.google.com/search?q='+searchg)

            # Launch software
            elif "open notepad" in query:
                speak("opening notepad")
                location = "C:\\Windows\\system32\\notepad.exe"
                notepad = subprocess.Popen(location)

            elif "ms word" in query:
                speak("opening ms word")
                mslocation = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                ms = subprocess.Popen(mslocation)

            elif "close notepad" in query:
                speak("closing notepad")
                notepad.terminate()

            elif "vs code" in query:
                speak("opening vs code")
                vslocation = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                vs = subprocess.Popen(vslocation)
            # Random jokes
            elif "joke" in query:
                speak(pyjokes.get_joke())

            elif 'open youtube' in query:
                try:
                    speak("what should i search in youtube")
                    searchyt=takeCommand().lower()
                    speak("opening youtube ")
                    wb.open('https://www.youtube.com/results?search_query='+searchyt)
                    speak("this is what i found")
                except Exception as e:
                    print(e)
                    speak("Sorry sir! I am not able to understand what u r saying .")

            elif "news" in query:
                news = wb.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                sleep(5)

            elif 'open whatsapp' in query:
                wb.open("whatsapp.com")

            elif 'play music' in query:
                music_dir = 'D:\\music'
                songs = os.listdir(music_dir)
                i=0
                i=random.randint(0,93)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[i]))

            elif "IP address" in query:
                geo()

            
            elif "whatsapp message" or "message" in query:
                whatsapp()

            elif "send email" in query:
                try:
                    speak("whom should i send the email")
                    speak("tell me the email pls!")
                    reciever=str(input("enter email sir:"))
                    speak("What should I say?")
                    content = takeCommand().lower()
                    to = reciever  
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")

            elif "bye" or "stop" in query:
                speak(" ok bye sir!")
                break


            # Logout/Shutdown/Restart
            # elif "logout" in query:
            #     speak('logging out in 5 second')
            #     sleep(5)
            #     os.system("shutdown - l")

            # elif "shutdown" in query:
            #     speak('shutting down in 5 second')
            #     sleep(5)
            #     os.system("shutdown /s /t 1")

            # elif "restart" in query:
            #     speak('restarting in 5 second')
            #     sleep(5)
            #     os.system("shutdown /r /t 1")

            







            sleep(3)


    except Exception:
        print("something went wrong!")
