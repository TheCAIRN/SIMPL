# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:49:11 2020

@author: Daniel


"""
import SIMPL_Parser as p  
from DataType import DataTypes as dtype

#TYPE = dtype()
sample_program = ["Create x as an integer array",
                "create y as an integer array",
                "create z as an integer array",
                
                "set x to 0 1 2 3 4 5 6 7 8 9",
                
                "create i as an integer",
                "while i is less than 10",
                
                "multiply i by 5",
                "append i to y",
                "divide i by 5",
                                
                "raise i to the 2nd power",
                "append i to z",
                "take the 2nd root of i",
                
                "add 1 to i",
                "close loop",
                
                "sort y ordered ascending",
                
                "remove the 1st element from y",
                "remove the 1st element from z",
                
                "plot x and y",
                "plot x and z",
                
                "get the standard deviation of z as d",
                "subtract 4 from d",
                
                "if d is inclusively between 10 and 20",
                "plot i and d"
                "also if d is exclusively outside 20 and 30",
                "say d",
                "otherwise",
                "join x to y",
                "print y",
                "close if"]


input_none = ["create x as an integer",
              "create y as an integer",
              "Set x to 5",
              "Set y to 20",
              "Multiply x by y",
              "Raise y to the 7th power",
              "If x is greater than 5",
                "If y is greater than 5",
                    "Set x to 100",
                "Also if y is less than 1",
                    "Set y to 1",
                "Otherwise",
                    "Set y to 2",
                "Close if",
            "Otherwise",
                "If y is less than 50",
                    "Set x to 3",
                "Otherwise",
                    "Set y to 4",
                "Close if",
            "Close if"]

input_while = ["create x as an integer",
               "Set x to 0",
               "while x is less than 10",
               "Add 1 to x",
               "Set y to x",
               "Raise y to the 2nd power",
               "print y",
               "Close loop"]

input_until = ["create x as an integer",
              "create y as an integer",
              "Set x to -1",
               "Set y to 1",
               "Until x is equal to 8",
               "Add 8 to x",
               "Subtract y from x",
               "Multiply y by 2",
               "print x",
               "Close loop"]

code = [line.lower() for line in input_until]
                   
class controlBlock:
    open_commands = ['if', 'for', 'while', 'until', 'test']
    parallel_commands = ['when', 'also', 'otherwise']
    
    loop_commands = ['for', 'while', 'until']
    
    def __init__(self, allcode):
        #code, depth, and cmd help parse the code
        self.code = allcode
        self.cmd = []
        self.depth = []
        
        #Lines of Code        
        self.LOC = len(allcode)
        
        self.logic_switch = {"if": self.__if__,
                             "close" : self.__close__,
                             "while" : self.__while__,
                             "until" : self.__until__,
                             "otherwise" : lambda l,d : [self.get_next_close(l,d), d]
                             }
        
        self.getStruct()
        #console structure
        self.printStruct()
        
    def getStruct(self):        
        depth = 0
        last_cmd = ""
        for line in self.code:
            cmd = line.split(" ")[0]
            
            #save line info
            self.cmd.append(cmd)
            if(cmd in self.open_commands): #sub blocks
                
                #save line info
                self.depth.append(depth)
                
                #increase block depth and register last cmd
                depth += 1
                last_cmd = cmd
                
            elif(cmd in self.parallel_commands): #parallel-depth blocks
                
                #save line info
                self.depth.append(depth-1)
                
                #register last cmd
                last_cmd = cmd
                
            elif(cmd == 'close'): #exit block
                
                #find new depth
                if(last_cmd == 'when'):
                    depth -= 2
                else:
                    depth -= 1
                
                #save line info
                self.depth.append(depth)
            else:
                #save line info
                self.depth.append(depth)
            
    def printStruct(self):
        for i in range(self.LOC):
            print(i, self.depth[i]*"-->" + self.code[i])
    
    def get_next_of_depth(self, l, d):
        for i in range(l, self.LOC):            
            if(self.depth[i] == d):
                return i
        raise Exception("Can't get next depth")
    
    def get_previous_of_depth(self, l, d):
        for i in range(l, 0, -1):
            if(self.depth[i] == d):
                return i
        raise Exception("can't get previous depth")
    
    def get_next_close(self, l, d):
        for i in range(l, self.LOC):
            if((self.cmd[i] == 'close') and (self.depth[i] == d)):
                return i
        raise Exception("can't get next close")
        
    def get_previous_open(self, l, d):
        for i in range(l, -1, -1):
            if((self.cmd[i] in self.open_commands) and (self.depth[i] == d)):
                return i
        raise Exception("can't get previous open")
        
    def __if__(self, l, d): #line, depth        
        #CONTROL FLOW: IF
        #On close, go to next line (skip parse)
        #On otherwise, enter block (skip parse)
        #If -> True, enter block
        #If -> False, recursively go to next "else"/"close"
        
        if(self.cmd[l] == 'close'):
            return [l+1, d-1]
        #get the if command (won't break anything if its not an if/elif)
        comparator = self.code[l].split('if ')
        if ((self.cmd[l] == 'otherwise') or p.parse(comparator[1])):
            return [l+1, d+1]
        else:
            return self.__if__(self.get_next_of_depth(l+1,d), d)  
    
    def __while__(self, l, d):
        comparator = self.code[l].split('while ')[1]
        if(p.parse(comparator)): #do while true
            return [l+1, d+1]
        else:
            return [self.get_next_close(l+1, d)+1, d]
    
    def __until__(self, l, d):
        comparator = self.code[l].split('until ')[1]
        if(not p.parse(comparator)): #do while false
            return [l+1, d+1]
        else:
            return self.get_next_close(l+1, d)+1, d
    
    def __close__(self, l, d):
        #head function is a loop      : go back and check the condition
        #              is a condition : go on
        blockHead = self.get_previous_open(l-1, d)
        if(self.cmd[blockHead] in self.loop_commands):
            return blockHead, d
        else:
            return l+1, d-1
    
    def run(self):
        line = 0
        depth = 0
      
        while(line < self.LOC):
            #print(self.code[line], line, depth)
            if(self.cmd[line] in self.logic_switch): #if its a logic command
                
                line, depth = self.logic_switch[self.cmd[line]](line, depth)
            else:
                p.parse(self.code[line])
                
                #continue if same depth, if < (exit function, if > is impossible without a function
                if((line+1 == self.LOC) or (self.depth[line] == self.depth[line+1])):
                    line += 1
                else:
                    #we look for the close because functions handle all cases, we are just trying to exit
                    depth -= 1
                    line = self.get_next_close(line+1, self.depth[line+1])
            
            #print("main", line, depth)
        
        print("Printing variables")
        print(p.get_vars())

#Front end will call this to run the code  
compiler = controlBlock(code)
compiler.run()
        