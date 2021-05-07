#For this section the youtube tutorial made by Tech with Tim went into detail on how to read text given with the google
# to text library.

# link to the video can be found at https://www.youtube.com/watch?v=-AzGZ_CHzJk&list=PLzMcBGfZo4-mBungzp4GO4fswxO8wTEFx&index=1
 #This program takes the text inputed on line 25 and uses the class speaking to read it as an MP3 file
#use commands in the command line
#pip install SpeechRecognition
#pip install gTTS
#pip install playsound

#importing the libraries
import os
import time
import playsound
import speech_recognition as speech_recognition
from gtts import gTTS

from tkinter import *

#creating a speech class
def speaking(text): #class speaking which takes in the data type of text
    text_speech = gTTS(text=text, lang = "en") #sets the parameters for what text and language
    filename = "inputvoice.mp3" # saves the text file of the mp3
    text_speech.save(filename)
    playsound.playsound(filename) #plays the mp3 file created in the filename variable

def intro_speaking(text): #class speaking which takes in the data type of text
    text2_speech2 = gTTS(text=text, lang = "en") #sets the parameters for what text and language
    filename_default2 = "intro_startvoice.mp3" # saves the text file of the mp3
    text2_speech2.save(filename_default2)
    playsound.playsound(filename_default2) #plays the mp3 file created in the filename variable

def start_speaking(text): #class speaking which takes in the data type of text
    text2_speech = gTTS(text=text, lang = "en") #sets the parameters for what text and language
    filename_default = "startvoice.mp3" # saves the text file of the mp3
    text2_speech.save(filename_default)
    playsound.playsound(filename_default) #plays the mp3 file created in the filename variable

#collecting the audio with the microphone using speech recognition library
def audio_input():
   rec = speech_recognition.Recognizer() #gets the speech recognizer
   with speech_recognition.Microphone() as source: #uses the microphone as the source for listening for the audio
        audio = rec.listen(source) #listens for the audio with microphone
        speech = ""

        try: #try and except is somewhat similar to if and else. Try means you try the code and if there are errors then it goes to except
            speech = rec.recognize_google(audio)
            print(speech)
            
            #this opens up a new window with tkinter and prints the words on the screen from the voice input
            window = Tk()

            text = Text(window)
            text.insert(INSERT, speech)
            text.config(state = "disabled")
            text.grid(row = 7, column = 1)

            window.mainloop()
        except Exception as e:
            print("Exception " + str(e))
   return speech

#speaking("Please begin speaking.") #submits the text into the mp3 file and prompts user to speak
#intro_speaking("Hello, welcome to SIMPL, a voice based programming language developed by Cairn university.")
#start_speaking("begin Talking")
#start_speaking("Let's Begin with a test, Please repeat this line: Create Variable X")


#text = audio_input() #begins to take the input by refrencing the audio input class
import SIMPL_Parser
print(SIMPL_Parser.parse("Create X as String"))

#Tim included this if statement where it takes the text said and if the text is in the string then it responds by speaking.
if "set" in text:
    import SIMPL_Parser
    # speaking("hi dan")
else:
    speaking("Please try again")
    audio_input()