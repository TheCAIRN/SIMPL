# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:21:37 2020

@author: Daniel
"""
import SIMPL_Interpreter as s_int
import ParserFunctionDefinitions as pfd
from DataType import DataTypes as dtype

TYPE = dtype()
TYPE.VARCONN = pfd.f.symbols

def get_vars():
    return pfd.f.symbols

def get_var(var):
    return pfd.f.symbols[var]



def parse (line_input):    
    #print(line_input)
    #make lowercase string
    line_input = line_input.lower()
    
    #get index of any commands 
    all_cmds = [[line_input.find(key), key] for key in pfd.commands]
    #all_cmds = [[line_input.find(key), key] for key in pfd.commands.keyis()]
     # The line above attempts to find keywords from the list of key words provided in pfd.commands.
    #get the primary command the user is using
    #This Command below is spitting an error and I'm not sure why. WHen we parse a command it explains that the list
    # index is out of range
    # After editing the command below from this:
    # cmd = pfd.commands[sorted([cmd for cmd in all_cmds if (cmd[0] >= 0)], key=lambda e: e[0])[0][1]]
    # to this:
    #cmd = pfd.commands[sorted([cmd for cmd in all_cmds if (cmd[0] >= 0)], key=lambda e: e[0])[0]]
    # We get a type error. TypeError: unhashable type: 'list' In other words we're cobining type list and key.
    # This might need a whole restructuring
    cmd = pfd.commands[sorted([cmd for cmd in all_cmds if (cmd[0] >= 0)], key=lambda e: e[0])[0][1]]
    #for testing purposes
    #print(cmd._str_())

    
    #seperate the data from the structure
    values = []
           
    for indx, key in enumerate(cmd.keywords):
        if(line_input.find(key) != 0):
            #get the parameter
            val = line_input[:line_input.find(key)]          
            #continue with the rest of the line
            line_input = line_input[len(val) + len(key):]
            
            values.append(val.strip())
        else:
            line_input = line_input[len(key):]
            
    #eventually the remaining will also be searched for flags
    if(line_input != ""):
        values.append(line_input.strip())    
    
    #print(values)
    
    #data to send to any given function
    data = {'obj' : None, 'param' : []}
    model = cmd.model.replace('C', '').replace('K', '')
    while(indx < len(values)):
        for indx, char in enumerate(model):
        #objects are variables in the system
            if(char == 'O'):
                #if it exists, send the name, otherwise error
                if((values[indx] in pfd.f.symbols) or (cmd.command in ['set', 'create'])):
                    data['obj'] = values[indx]
                else:
                    raise Exception("Cannot find variable %s" % values[indx])
        #parameters can be variables in the system or things to be casted
            elif (char == 'P'):
                #if it is a variable, sent it, otherwise cast to the right type
                if(values[indx] in pfd.f.symbols):
                    if(cmd.parameters[indx] >= 6):
                        data['param'].append([pfd.f.symbols[values[indx]]])
                    else:
                        data['param'].append(pfd.f.symbols[values[indx]])
                else:
                    #do type casting
                    if(data['obj'] in pfd.f.symbols):
                        data['param'].append(TYPE.cast(values[indx], cmd.parameters[indx], pfd.f.symbols[data['obj']]))
                    else:
                        data['param'].append(TYPE.cast(values[indx], cmd.parameters[indx], None))
                    
    #print(data)
    out = cmd.function(data)
    #print(get_vars())
    return out
