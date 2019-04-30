# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 23:24:14 2019

@author: sw344
"""
import SIMPL_Processor


class Parser:
        pr = SIMPL_Processor.SIMPL_Processor()
        def Parse(input):
            input == (input.split(" "))
        
    #Management Commands
        
    #Open Project and Open new Project
        if input[0] == "Open":
            if input[1] == "Project":
                pr.open_project(input [2])
        elif input[1] == "New":
           pr.create_project(input [3])
        
    #Save Project with name
        if input[0] == "Save":
            if input[1] == "Project":
                pr.save_project(input [2])
        
    #Run Project(must already be in file with soemthing to run, error should come from processor)
        if input[0] == "Run":
            pr.run_project
        
        
    #Navigation Commands
        
    #Read line|lines command needs some more decisions before progress can continue
        if input[0] == "Read":
            if input[1] == "Line":
                pr.line(input [2])
        
    #Reads Mulitple Lines
        if input[1] == "Lines" and (lenInput) == 5:
            if input[4] == "End":
                pr.readEnd
        elif input [3] == "TO":
           pr.readLines
                
        
    #NEED FUNCTION FOR STOP IN PROCESSOR   
        if input[0] == "Stop":
             
    #NEED FUNCTIONS FOR THESE COMMANDS GOT TO THE BEGINNING OR END OF A LINE  
        if input[0] == "Go":
            if input[3] == "Beginning":
               pr.beginLine
            elif input[3] == "End":
                pr.endLine
    
    
    #NEED FUNCTION FOR THIS? 
        if input[0] == "Change":
            if input[1] == "Line":
                if input[3] == "To":
                    parm2 == ' '.join(input[4:])
                    pr.change(input[2], parm2)
            
        
    #Input Commands
    
    #Create Variables and Create Array
        if input[0] == "Create":
            if input[1] == "Variable":
                pr.create_variable(input [2])
            elif input[1] == "Array":
                pr.create_array(input [2])
                if input[3] == "Includes":
                    pr.assign_value(input[2],input[4])
        
    #Sort Numerically and Alphabetically
        if input[0] == "Sort":
            if input[2] == "Numerically":
                pr.numSort (input[1])
        
        if input[0] == "Sort":
            if input[2] == "Alphabetically":
                pr.alphSort (input[1])
    
    #Set values for variables or arrays
     #I believe this command may need to be changed in the processor from assign value to set value   
        if input [0] == "Set":
            pr.assign_value(input [2])
        
    #Separate by a certain character etc.     
    #NEED FUNCTION FROM THE PROCESSOR FOR THIS?  
        if input [0] == "Separate":
            if input[3] == "By":
                pr.separate
        
    #User can generate comments    
    #NEED FUNCTION FROM THE PROCESSOR FOR THIS How do I do the END COMMENT?  
        if input [0] == "Comment":
            pr.comment
        
    #Join things together      
        if input [0] == "Join":
            if input.length == 6:
                pr.join(input[1],input[3], input[5])
            elif input.length == 4 and input[2]=="to":
                pr.join(input[1],input[3])
            else:
                pr.throw_error("Bad")
        
    #Output Commands:
      
    #Say and Print will call the say function just with a different parameter to differ between the two. Did I do this corectly? 
    #Say for the program to be read back to the user   
        if input[0] == "Say":
            pr.say(input[1])
    #Print for Print command to be inserted or for testing scripts?    
        if input[0] == "Print":
            pr.say(input[0])
        
            
        
        
        
