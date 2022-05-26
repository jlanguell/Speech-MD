# Listens For and Handles Audio Input, then Translates it & Passes it to Markdown

# Imports
import speech_recognition as sr
import pyttsx3
import sys
from data_write import *

# Variables
engine = pyttsx3.init()
engine.setProperty('rate', 200)
engine.setProperty('volume', 0.9)
r = sr.Recognizer()


def engine_translate(device, file, box, status):

    # status = None
    try:
        # Designates device & audio gathering params to use
        speech = sr.Microphone(device_index=device, sample_rate=20000)

    except AttributeError:

        print("Please install the correct pyaudio wheel for your project. Link in references.txt.")
        sys.exit()

    with speech as source:

        # Dynamically determine ambience/speech
        #r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = False

        # Seconds before an API request is tossed due to no response
        r.operation_timeout = 20

        # Seconds of silence after speaking before listen() is ended
        r.pause_threshold = 1

        try:
            # Variable, when used, begins listening to selected source
            audio = r.listen(source, timeout=3)
            ''', phrase_time_limit=3)'''

            # Variable to store/make text data translated from listen() source -> API request -> API response
            recog = r.recognize_google(audio, language='en-US')

            # Toggle between SpeechMD Writing Data/Listening for pause/resume commands
            if recog == 'system pause':
                engine.say("Speech to em dee has been paused.")
                engine.say("Please press 'r' to resume.")
                print("Speech-MD has been PAUSED")
                status = 0
                # Ensures engine finishes processing callbacks/commands
                engine.runAndWait()

            # Write data function call
            if status != 0:
                print("You said: " + recog)
                # engine.say("You said: " + recog)
                write(file, recog, box)

            # Toggle between SpeechMD Writing Data/Listening for pause/resume commands
            while status == 0:
                resume = input("Please input 'r' to resume: ")

                if resume.lower() == 'r':
                    engine.say("Speech to em dee has been resumed.")
                    print("Speech-MD has been RESUMED")
                    # Ensures engine finishes processing callbacks/commands
                    engine.runAndWait()
                    status = 1


        # Google Speech Recognition Errors
        except sr.UnknownValueError:
            engine.say("Google Speech could not understand the audio")
            engine.runAndWait()
            pass

        except sr.RequestError as e:
            engine.say("There was an issue requesting results from Google Speech; {0}".format(e))
            engine.runAndWait()
            pass
        except sr.WaitTimeoutError:
            pass

        # Recursively call function to actively run the application and maintain status code
        # engine_translate(device, file, box, status)
        return
