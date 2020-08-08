from __future__ import unicode_literals  
import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import youtube_dl
import urllib
import shutil
from pathlib import Path
import requests
import time


engine = pyttsx3.init()
'''len(voices)-1'''

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(audio):
    print('Chitty ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi Pavi,Good Morning! The time is',currentH)

    if currentH >= 3 and currentH < 15:
        speak('Hi Pavi,Good Afternoon!')

    if currentH >= 15 and currentH !=19:
        speak('Hi Pavi,Good Evening!')

    if currentH >= 19 and currentH !=10:
        speak('Good Night Pavi! It is night...Sweet Dreams!!')
        speak ('May i help you?')

greetMe()

speak('I am your assistant Chitty ,How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        r.pause_threshold =  0.5
    try:
        query = r.recognize_google(audio).lower()
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry Pavi! TRY Writing your command Pavi')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

            
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Pavi! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query or 'bye' in query:
            speak('okay')
            speak('Bye Pavi, have a good day.')
            sys.exit()

        elif 'what time is it' in query or 'what is the time Chitty' in query or 'what time is it' in query or 'time' in query or 'current time' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'what date is it' in query or 'what is the date Chitty' in query or 'what date is it' in query or 'date' in query or 'current date' in query:
            speak('The current time is '+(str(datetime.datetime.now().strftime('%H:%M:%S'))))

        elif 'hello' in query:
            speak('Hello Pavi')

                                    
        elif 'play music' in query or 'play songs' in query or 'play songs Chitty' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play english music' in query or 'play english songs' in query or 'play english songs Chitty' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Alex_Sparrow-sheiscrazybutsheismine','wedont','Konjam','stressedout']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play tamil music' in query or 'play tamil songs' in query or 'play tamil songs skava' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['Konjam']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)

        elif 'play hindi music' in query or 'play hindi songs' in query or 'play hindi songs skava' in query:
            music_folder = 'S:\\AI\\music\\'
            music = ['ikvaariaa']
            random_music = music_folder + random.choice(music) + '.mp3'
            speak('Okay, here is your music! Enjoy!')
            
            os.system(random_music)
        elif 'download youtube' in query:
            ydl_opts = {}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([input()])
        elif 'download pdf' in query:
            filename = Path('DAA.pdf')
            url = input("Enter the link")
            res= requests.get(url)
            filename.write_bytes(res.content)
        

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
        
        elif "Tell me motivation Quotes" in query or 'motivate me' or 'say motivational quotes' or 'sad' or 'unhappy' in query:
            stMsgs = ['Failure will never overtake me if my determination to succeed is strong enough',
                      'The past cannot be changed. The future is yet in your power',
                      'Only I can change my life. No one can do it for me',
                      'Change your life today. Don\'t gamble on the future, act now, without delay',
                      'Do the difficult things while they are easy and do the great things while they are small. A journey of a thousand miles must begin with a single step',
                      'Either I will find a way, or I will make one',
                      'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time',
                      'Good, better, best. Never let it rest. Till your good is better and your better is best']
            highMsgs = ['Dont worry dude,every hard time comes to an end']
            speak(random.choice(stMsgs))
            speak('I think thins Motivated You Pavi ... if Not')
            speak(random.choice(highMsgs))
            speak('You will be happy in few minutes watch this')
            webbrowser.open('https://www.youtube.com/watch?v=20p6inVwjbI')
            time.sleep(60)
            speak('I think you cool now!!')

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('google says - ')
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('any Command! Pavi!')

