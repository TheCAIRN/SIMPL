# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:24:14 2019

@author: sw344
"""
class Parser:
def Parse(input):
input = (input.split(" "))
    
    #Management Commands
    
    #Open Project and Open new Project
    if input[0] = "Open":
        if input[1] = "Project":
        return open_project(input [2])
    elif input[1] = "New"
    return create_project(input [3])
    
    #Save Project with name
    if input[0] = "Save":
        if input[1] = "Project"
        return save_project(input [2])
    
    #Run Project(must already be in file with soemthing to run, error should come from processor)
    if input[0] = "Run":
        return run_project
    
    
    #Navigation Commands
    
    #Read line|lines command needs some more decisions before progress can continue
    if input[0] = "Read":
        if input[1] = "Line"
        return line(input [2])
    
    #Reads Mulitple Lines
    if input[1] = "Lines" && input.length == 5:
        if input[4] == "End"
        return lines
        
    
    return read_lines
    
    
 #NEED FUNCTION FOR STOP IN PROCESSOR   
    if input[0] = "Stop":
        return 
    
    if input[0] = "Beginning":
        
    
    #Input Commands
    if input[0] = "Create":
        #Do I need a return here?
        if input[1] = "Variable":
            return create_variable(input [2])
        elif input[1] = "Array":
            return create_array(input [2])
    
    
    if input[0] = "Sort":
        return sort (input[2])
    
 #I believe this command may need to be changed in the processor from assign value to set value   
    if input [0] = "Set":
        return assign_value(input [2])
    
  #NEED FUNCTION FROM THE PROCESSOR FOR THIS  
    if input [0] = "Separate":
        return 
    
   #NEED FUNCTION FROM THE PROCESSOR FOR THIS  
    if input [0] = "Comment":
        return comment
    

        
    if input [0] = "Join":
        if input.length == 6:
          join(input[1],input[3], input[5])
          elif input.length == 4 and input[2]=="to":
              join(input[1],input[3])
              else:
                  throw_error("Bad")
    
    
    
        
    
    
    
