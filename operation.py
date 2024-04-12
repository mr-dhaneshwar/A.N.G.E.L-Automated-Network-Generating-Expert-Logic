from requests import get
import pyautogui as p
from openapi import *
from speech import *
import webbrowser
from mail import *
import random


def task():
    import pywhatkit as kit
    '''
     function that contains a loop which executes tasks according to the spoken command.

    '''

    while True:
        query = takeCommand().lower()
        if error(query):
            continue

        # Logic for executing tasks on query
        if query in bye:
            if 'wait' in query:
                speak('ok i am waiting...')
                break
            else:
                speak('ok bye, i am going to sleep')
                break

        elif 'how are you' in query:
            speak(random.choice(thanks))
            speak('What i can do for you')

        elif 'open google' in query:

            webbrowser.open('google.com')
            speak('opening google')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
            speak('opening youtube')

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')
            speak('opening stack overflow')

        elif 'open' in query:
            query = query.replace('open', '').strip()
            p.hotkey('Win')
            for i in query:
                p.hotkey(i)
            p.hotkey('enter')
            speak('opening,' + query)

        elif 'switch' in query and 'window' in query:
            speak('ok')
            p.hotkey('Alt', 'Tab')

        elif 'close' in query and 'window' in query:
            speak('ok')
            p.hotkey('Alt', 'F4')

        elif ('screenshot' in query or 'screen shot' in query) and 'show' in query:
            p.hotkey('win', 'g')
            speak('here is your screenshots')

        elif ('screenshot' in query or 'screen shot' in query) and ('take' in query or 'get' in query):
            speak('ok')
            p.hotkey('Win', 'Alt', 'writeScreen')
            speak('screenshot seved')

        elif 'time' in query:
            speak(current_time() + ' ')

        elif 'play' in query and ('music' in query or 'song' in query):
            speak('which song ?')
            song = takeCommand(1)
            speak('opening youtube')
            kit.playonyt(song)
            break

        elif 'email' in query or 'mail' in query:
            try:
                to_list = (query.split('to'))
                to = to_list[1].strip()

                if check_mail(to):
                    to = check_mail(to)
                    speak('what is the message')
                    msg = takeCommand().lower()
                    sendEmail(to[1], msg)  # 1st index gives email
                    # 0 index gives name
                    speak(f'message has been send to {to[0]}', 1)
                else:
                    speak('email address not found', 2)

            except Exception as e:
                print('problem while sending email', e)
                speak('email not send try again...', 2)

        elif 'sleep' in query and ('laptop' in query or 'pc' in query):
            speak('ok')
            p.hotkey('Win', 'd')
            p.hotkey('Alt', 'F4')
            p.hotkey('up')
            p.hotkey('Enter')
            return

        elif 'shutdown' in query and ('laptop' in query or 'pc' in query):
            p.hotkey('win', 'd')
            p.hotkey('Alt', 'F4')
            speak('Shutting down')
            p.hotkey('Enter')

        elif 'restart' in query and ('laptop' in query or 'pc' in query):
            p.hotkey('win', 'd')
            p.hotkey('Alt', 'F4')
            speak('Shutting down')
            p.hotkey('down')
            p.hotkey('Enter')

        elif 'ip address' in query and 'my' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP Address is {ip}')

        elif 'angel' in query:
            query = query.replace('angel ', '') + '.'
            speak('Please wait few seconds, I am searching...', 5)
            speak(angel(query), 4)

        else:
            speak('Please wait few seconds, I am searching...', 5)
            speak(angel(query), 4)
