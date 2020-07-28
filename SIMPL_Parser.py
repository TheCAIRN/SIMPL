# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:42:02 2020

@author: Daniel
"""

import speech_recognition as sr
import numpy as np
#------------------------------------------Sample Functions-------------------------------------------------------------
def addition(obj, parameters):
    BUILT_IN_VARIABLES[obj] += sum(parameters)

def multiplication(obj, parameters):
    BUILT_IN_VARIABLES[obj] *= np.prod(parameters)

def set_value(obj, value):
    BUILT_IN_VARIABLES[obj] = value
#------------------------------------------Definitions------------------------------------------------------------------
class function:
    def __init__(self, name, keyword, model, parameters, call):
        #class to manage the parsing of specific functions
        self.name = name
        self.keyword = keyword
        self.model = model
        self.parameters = parameters
        self.call = call

#each function has specific order and keywords that make it sound natural
add = function("add", "to", "CPKO", "inta,int", addition)
multiply = function("multiply", "by", "COKP", "int,inta", multiplication)
set_func = function("set", "to", "COKP", "int,int", set_value)

#current list of commands that work
BUILT_IN_COMMANDS = {"add" : add,
                     "multiply" : multiply,
                     "set" : set_func}

x = 1
y = 5
BUILT_IN_VARIABLES = {"x" : x,
                      "y" : y}

#------------------------------------------Parser------------------------------------------------------------------
def parse (input):    
    print(input)
    #make lowercase string
    input = input.lower()
    
    #split into words
    words = input.split(" ")
    
    #get command function and remove from list
    command = BUILT_IN_COMMANDS[words.pop(0)]
    
    #split between the parameters and variable
    key_values = " ".join(words).split(command.keyword)
    #get the parameter requirements
    param_type = command.parameters.split(",")
    
    #Models:
    #CPKO - Command Parameter Keyword Object
    #COKP - Commands Object Keyword Parameter
    #using the model, get the variable and the parameters
    index = 0
    for letter in command.model:
        if(letter == "O"):
            #remove spaces and get the string version of the object
            obj = key_values[index].strip(" ")
            index += 1
        if(letter == "P"):
            #remove spaces and get the parameters
            pval = key_values[index].strip(" ")
            #only turn into a list if there are enough elements (saves hasle later)
            if(pval.find(" ") > 0):
                pval = pval.split(" ")
            parameters = check_type(pval, param_type[index])
            index += 1
    #call the function
    print(parameters, obj)
    command.call(obj, parameters)
    print(BUILT_IN_VARIABLES[obj])

#------------------------------------------Helper Function------------------------------------------------------------------
def check_type(value, pattern):
    try:
        #turn the input string into the specifed type
        if(pattern == "int"):
            #if it's a number string, just convert it
            if(value.isnumeric()):
                value = int(value)
            
        if(pattern == "inta"):
            if(type(value) == type([])):
                value.remove("and")
                out = []
                for i in value:
                    if(i.isnumeric()):
                        out.append(int(i))
                    else:
                        out.append(BUILT_IN_VARIABLES[i])
                value = out
            else:
                #if it's a number string, just convert it
                if(value.isnumeric()):
                    value = [int(value)]
                else:
                    #if not, its a variable, get it
                    value = [BUILT_IN_VARIABLES[value]]
    except:
        print("Error: Expected %s, Recieved %s" % (pattern, type(value)))
    return value

def get_variable(name, pattern):
    #do type checking ?
    return BUILT_IN_VARIABLES[name.strip(" ")]
    
#------------------------------------------Audio------------------------------------------------------------------
#parse("Set y to 4")
#parse("Multiply x by y")
#parse("Add 1 y 3 4 and x to y")

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
