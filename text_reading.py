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

#creating a spe
def speaking(text): #class speaking which takes in the data type of text
    text_speech = gTTS(text=text, lang = "en") #sets the parameters for what text and language
    filename = "inputvoice.mp3" # saves the text file of the mp3
    text_speech.save(filename)
    playsound.playsound(filename) #plays the mp3 file created in the filename variable

speaking("Hello Daniel DeCarlo") #submits the text into the mp3 file
