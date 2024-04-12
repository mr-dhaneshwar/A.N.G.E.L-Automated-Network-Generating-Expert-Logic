import speech_recognition as sr
import pyttsx3
import datetime
from threading import *
from translator import *


# from offtake import*
import time
# Define All reply
thanks = ['i am fine ', 'always there for you ',
          'i am good , thanks for asking ', 'fine ', 'i am good']
bye = ['goodbye angel', 'bye angel', 'bye', 'okay bye', 'okay bye angel', 'goodbye', 'chup ho jao', 'quit',
       'quit Angel', 'wait', 'okay wait']
start = ['angel', 'wake up angel', 'hey angel', 'hello angel']
angel_output = ['yes boss i am here', 'always here for you ', 'ready ']

# Initializes the pyttsx3 module. The SAPI5 helps to convert text to speech.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # Gets the list of voices available.


def error(query):
    '''
    function that checks if the query is blank or not and returns either True or False.

    '''
    if query == '':  # checks if the query is blank or not
        speak('I did not understand, please Say That again.... ', 2)
        return True
    return False


def current_time():
    '''
    function that returns the current time in a string.

    '''
    strTime = datetime.datetime.now().strftime('%I:%M')  # detect hours and minits
    hour = int(datetime.datetime.now().hour)  # getting hours
    if hour >= 0 and hour < 12:  # check current time is AM or PM
        return f"it's {strTime}AM"
    else:
        return f"it's {strTime}PM"


def speak(audio, img=1):
    '''
    function that takes an audio string and plays it back using the pyttsx3 module.
    '''
    global speak_status, theme
    try:

        x = 1  # get the language
        if x == 1:
            audio = to_mr(audio)
        elif x == 2:
            audio = audio
        else:
            audio = to_hi(audio)

        
        print(('Angel: ' + audio))

        print('Angel: ' + audio)
        # if speak_check():
            # if get_lang() == 2:
            #     # Sets the voice to the third option in the list.
            #     engine.setProperty('voice', voices[4].id)
            # else:
            #     # Sets the voice to the second option in the list.
            #     engine.setProperty('voice', voices[1].id)
        if 1:
            engine.setProperty('voice', voices[4].id)
            engine.setProperty('rate', 195)
            engine.say(audio)
            engine.runAndWait()

    except Exception as e:
        print('speak problem....\n', e)


def takeCommand(l=0):
    global lang
    '''
    function that listens to the microphone and recognizes the speech using Google Speech Recognition.

    '''

    # creates an instance of the SpeechRecognizer class from the SpeechRecognition library
    r = sr.Recognizer()
    x = 1  # get the language
    if x == 1:
        slang = 'mr'
    elif x == 2:
        slang = 'en-in'
    else:
        slang = 'hi'
    try:
        with sr.Microphone() as source:
            print('Listning....')
            r.adjust_for_ambient_noise(source)
            r.phrase_threshold = 1
            r.energy_threshold = 600
            r.dynamic_energy_threshold = True
            audio = r.listen(source, timeout=10)
        try:
            print('Recognizing....')

            query = r.recognize_google(
                audio, language=slang, show_all=False, key=None)
            print(f'you: {query}')

        except Exception as e:
            query = ''
            return query
        if l == 1:
            return query
        else:
            return to_en(query)
    except Exception as e:
        print('listen problem......', e)


takeCommand()