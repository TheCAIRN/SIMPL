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
        return readEnd
    elif input [3] == "TO" :
        return readLines
        
    
    
 #NEED FUNCTION FOR STOP IN PROCESSOR   
    if input[0] = "Stop":
        return 
# NEED FUNCTIONS FOR THESE COMMANDS GOT TO THE BEGINNING OR END OF A LINE  
    if input[0] = "Go":
        if input[3] == "Beginning"
        return beginLine
    elif input[3] == "End"
    return endLine


#NEED FUNCTION FOR THIS! This is also missiong something on how to actually change the line through a command???
    if input[0] = "Change":
        if input[1] == "Line"
        if input[3] == "To"
            return change
        
    
    #Input Commands
    
    #How do I get the included values into the array once created? 
    if input[0] = "Create":
        #Do I need a return here?
        if input[1] = "Variable":
            return create_variable(input [2])
        elif input[1] = "Array":
           
            return create_array(input [2])
    
    
    if input[0] = "Sort":
        if input[2] = "Numerically"
        return numSort (input[1])
    
    if input[0] = "Sort":
        if input[2] = "Alphabetically"
        return alphSort (input[1])
    
 #I believe this command may need to be changed in the processor from assign value to set value   
    if input [0] = "Set":
        return assign_value(input [2])
    
  #NEED FUNCTION FROM THE PROCESSOR FOR THIS  
    if input [0] = "Separate":
        if input[3] == "By"
        return separate
    
   #NEED FUNCTION FROM THE PROCESSOR FOR THIS How do I do the END COMMENT?  
    if input [0] = "Comment":
        return comment
    

        
    if input [0] = "Join":
        if input.length == 6:
          join(input[1],input[3], input[5])
          elif input.length == 4 and input[2]=="to":
              join(input[1],input[3])
              else:
                  throw_error("Bad")
    
  #Output Commands:
  
  # Say and Print will call the say function just with a different parameter to differ between the two. Did I do this corectly? 
    if input[0] = "Say":
        return say(input[1])
    
    if input[0] = "Print":
        return say(input[0])
    
        
    
    
    
