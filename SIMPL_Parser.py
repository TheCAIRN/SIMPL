# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:42:02 2020

@author: Daniel
"""

import speech_recognition as sr
import builtin as internal
#------------------------------------------Parser------------------------------------------------------------------
def parse (input):    
    print()
    #make lowercase string
    input = input.lower()
    
    #seperate the command from the rest of the input
    #all current command begin with C
    cmd = input[:input.find(" ")]
    input = input[len(cmd) + 1:]
    
    #get the command the user is using
    command = internal.commands[cmd]
    
    #seperate the data from the structure
    values = []        
    for key in command.keywords:
        val = input[:input.find(key)]
        input = input[len(val) + len(key):]
        values.append(val.strip())
    #eventually the remaining will also be searched for flags
    if(input != ""):
        values.append(input.strip())    
    
    command.run(values)
