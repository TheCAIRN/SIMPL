# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:24:14 2019

@author: sw344
"""
class Parser:
def Parse(input):
input = (input.split(" "))
    
    #Management Commands
    if input[0] = "Open":
        return open_project
        elif input [1] ="New"
            return #NEED METHOD FOR THIS
    
    
    if input[0] = "Save":
        return save_project
    
    
    if input[0] = "Run":
        return run_project
    
    
    #Navigation Commands
    if input[0] = "Read":
        return #NEED FUNCTION. HAS TO CONNECT TO LINE?
    #WHAT SHOULD I DO FOR LINE?
    
    if input[0] = "Stop":
        return #NEED FUNCTION
    
    #Input Commands
    if input[0] = "Create":
        #Do I need a return here?
    elif input[1] = "Variable":
        return create_variable(input [2])
    elif input[1] = "Array":
        return create_array(input [2])
    
    
    if input[0] = "Sort":
        return sort
    
    
    if input [0] = "Set":
        return assign_value(input [2])
    
    
    if input [0] = "Separate":
        return separate
    
    
    if input [0] = "Comment":
        return comment
    

        
    if input [0] = "Join":
    if input.length == 6:
       join(input[1],input[3], input[5])
   elif input.length == 4 and input[2]=="to":
       join(input[1],input[3])
   else:
        throw_error("Bad")
    
    
    
        
    
    
    
