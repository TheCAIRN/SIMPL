# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:42:02 2020

@author: Daniel
"""

import speech_recognition as sr
import numpy as np
#------------------------------------------Sample Functions-------------------------------------------------------------
def addition(obj, parameters):
    return obj + sum(parameters)

def multiplication(obj, parameters):
    return obj * np.prod(parameters)

def set_value(obj, value):
    return value
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

#sample variables until I make a "create variable" command
x = 1
y = 1
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
            val = key_values[index].strip(" ")
            obj = get_variable(val, param_type[index])
            index += 1
        if(letter == "P"):
            #remove spaces and get the parameters
            val = key_values[index].strip(" ")
            #only turn into a list if there are enough elements (saves hasle later)
            if(val.find(" ") > 0):
                val = val.split(" ")
            parameters = check_type(val, param_type[index])
            index += 1
    #call the function
    BUILT_IN_VARIABLES[obj] = command.call(obj, parameters)
    print(BUILT_IN_VARIABLES[obj])

#------------------------------------------Helper Function------------------------------------------------------------------
def check_type(value, pattern):
    #turn the input string into the specifed type
    if(pattern == "int"):
        if(type(value) == "list"):
            #incompatable, can't be a list
            print("Error: Expected %s, Recieved %s" % (pattern, type(value)))
        else:
            #if it's a number string, just convert it
            if(value.isnumeric()):
                value = int(value)
            else:
                #if not, its a variable, get it
                value = get_variable(value, pattern)                
            
    if(pattern == "inta"):
        if(type(value) == type([])):
            value.remove("and")
            value = [int(i) for i in value]
        else:
            #if it's a number string, just convert it
            if(value.isnumeric()):
                value = [int(value)]
            else:
                #if not, its a variable, get it
                value = [get_variable(value, pattern)]
    return value

def get_variable(name, pattern):
    #do type checking ?
    return BUILT_IN_VARIABLES[name.strip(" ")]
    
#------------------------------------------Audio------------------------------------------------------------------
#the issue here is that x and y don't keep their values. I can't seem to pass by reference (7/26)
parse("Set y to 4")
parse("Multiply x by y")
parse("Add x to y")

