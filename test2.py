import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Set to a different voice (change index accordingly)
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate', 205)
engine.say("Here's a Python script for text-to-speech (TTS) that supports multiple voices and languages.")
# engine.say("मैं आपकी किस प्रकार सहायता कर सकता हूँ ?")
engine.runAndWait()
