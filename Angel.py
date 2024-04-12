# A.N.G.E.L : Automated Network Generating Expert Logic

# Importing necessary modules
from operation import *  # importing functions from operation module
from threading import *  # importing threading module
import pyautogui as p   # importing pyautogui module as 'p'
import socket            # importing socket module for checking internet connection status
import random            # importing random module for generating random outputs
import sys

# Function to check internet connection status


def internet_connection_status():
    try:
        # Tries to create a connection with Google's web server on port 80
        socket.create_connection(("www.google.com", 80))
        return True  # returns True if connection is successful
    except OSError:
        return False  # returns False if connection is unsuccessful

# Function to greet the user


def wishMe():
    speak('Hello dear')  # speaks 'Hello dear'
    hour = int(datetime.datetime.now().hour)  # gets current hour
    if 0 <= hour < 12:  # checks if it's morning
        speak('Good Morning')  # speaks 'Good Morning'
    elif 12 <= hour < 18:  # checks if it's afternoon
        speak('Good Afternoon')  # speaks 'Good Afternoon'
    else:  # if it's not morning or afternoon, it's evening
        speak('Good Evening')  # speaks 'Good Evening'
    speak(current_time())  # speaks current time
    speak('my name is Angel, How may I assist you today?')  # speaks introduction


open = 0  # initializes variable 'open' to 0


def main():
    global open  # makes 'open' variable global
    if internet_connection_status():  # checks internet connection status
        try:
            set_img(1)
            while True:  # runs an infinite loop

                query = takeCommand().lower()  # gets user's query and converts it to lower case

                if 'goodbye' in query or 'bye' in query:  # checks if query is a goodbye command
                    # speaks a goodbye message with a delay of 6 seconds
                    speak('goodbye, Love you 3000....', 6)
                    close()  # closes the program
                    return

                # checks if query is a start command or includes 'angel'
                if query in start or 'angel' in query or 'hello' in query:
                    set_img(2)
                    p.hotkey('up')  # scrolls up to the top of the screen
                    if query == 'angel':  # checks if query is 'angel'
                        # speaks a random output from 'angel_output' list
                        speak(random.choice(angel_output))
                        task()  # calls 'task' function
                    else:
                        if open == 0:  # checks if 'open' variable is 0
                            wishMe()  # calls 'wishMe' function
                            task()  # calls 'task' function
                        else:
                            # speaks a prompt message
                            speak('How may I assist you ?')
                            task()  # calls 'task' function

                open = 1  # sets 'open' variable to 1
        except Exception as e:
            print("error to start...", e)  # prints error message if any
            show_error(e)
    else:
        msg = 'You are not connected to the internet'
        speak(msg, 2)  # speaks the message with a delay of 2 seconds
        show_error(msg)


my_window(main)  # creates a window and runs the 'main' function
sys.exit()  # exits the program after the window is closed
