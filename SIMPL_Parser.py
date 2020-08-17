# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:49:11 2020

@author: Daniel


"""
import functions as process

#------------------------------------------Command Linguistics-----------------------------------------------------
#Command Object [Keyword Paramater]         "Set y to 10" 
#Command [Parameter Keyword] Object         "Add 5 to x"
#
#                                           "if x is greater than 3 then"
#
#
#
#
#------------------------------------------Parser------------------------------
def parse (line_input):    
    
    #make lowercase string
    line_input = line_input.lower()
    
    #get index of any commands 
    all_cmds = [[line_input.find(key), key] for key in commands.keys()]
    
    #get the primary command the user is using
    command = commands[sorted([cmd for cmd in all_cmds if (cmd[0] >= 0)], key=lambda e: e[0])[0][1]]
    
    
    #cmd = line_input[:line_input.find(" ")]
    #line_input = line_input[len(cmd) + 1:]
    #command = commands[cmd]
    
    #seperate the data from the structure
    values = []        
    for key in command.keywords:
        if(line_input.find(key) != 0):
            val = line_input[:line_input.find(key)]
            line_input = line_input[len(val) + len(key):]
            
            values.append(val.strip())
        else:
            line_input = line_input = line_input[len(key):]
            
    #eventually the remaining will also be searched for flags
    if(line_input != ""):
        values.append(line_input.strip())    
    
    
    #do type casting
    if(command.command == "set"):
        values[0] = values[0]
        values[1] = type_check(values[1], get_type(values[0]))
    else:
        i = 0
        for m in command.model:
            if(m == "P"):
                values[i] = type_check(values[i], command.parameters[i])
            
            if(m in ['P', 'O']):
                i += 1
                               
    #print("var dummp", values)
    #print("called %s" % command.command)
    return command.function(values)

#------------------------------------------Definitions-------------------------
class profile:
    def __init__(self, command, keywords, model, parameters, function):
        #class to manage the parsing of specific functions
        self.command = command
        self.keywords = [command] + keywords
        self.model = model
        self.parameters = parameters
        self.function = function       

#--------------------------------Casting--------------------------------
def get_type(var):
    vtype = str(type(var))
    if('int' in vtype):
        return 'int'
    if('str' in vtype):
        return 'str'
    if('list' in vtype):
        return get_type(var[0]) + " arr"
    

def type_check(var, vtype):
    return switch[vtype](var)
    
def t_int(var):
    if(var.isnumeric()):
        return int(var)
    else:
        return process.variables[var]

def t_str(var):
    return var

def t_any(var):
    return var

def t_int_arr(var):
    var = var.split(" ")
    
    if("and" in var):
        var.remove("and")
        
    tmp = []
    for v in var:
        #print(v)
        if(v.isnumeric()):
            tmp.append(int(v))
        else:
            tmp.append(process.variables[v])
    return tmp[:]
    
def t_str_arr(var):
    var = var.split(" ")
    if("and" in var):
        var.remove("and")
    return var

def t_any_arr(var):
    return var
    
#switch for type casting
#float, bool, list, int, str
switch = {"int" : t_int,
          "str" : t_str,
          "any" : t_any,
          "int arr" : t_int_arr,
          "str arr" : t_str_arr,
          "any arr" : t_any_arr}

#--------------------------------Logic Flow-----------------------------
def logic_if(args):
    #Allow for "If" and "And if" 
    #line update
    return(parse(args[-1]))

def logic_otherwise(args):
    #no condition, always true
    return True
    
def logic_test(args):
    #always enter
    return True

def logic_when(args):
    #get result
    return(parse(args[0]))
    
def greater(args):
    #see if element 0 is greater than element 1
    print(args[0] > args[1])
    return args[0] > args[1]

def greater_or_equal(args):
    #see if element 0 is greater than or equal toelement 1
    print(args[0] >= args[1])
    return args[0] >= args[1]

def less(args):
    #see if element 0 is less than element 1
    print(args[0] < args[1])
    return args[0] < args[1]

def less_or_equal(args):
    #see if element 0 is less than or equal to element 1
    print(args[0] <= args[1])
    return args[0] <= args[1]

def equal(args):
    #see if element 0 is equal to element 1
    print(args[0] == args[1])
    return args[0] == args[1]
#--------------------------------Function Profiles-----------------------------

#each function has specific order and keywords that make it sound natural

#MATH
add = profile("add", ["to"], "CPKO", ["int arr", "int"], process.add)
multiply = profile("multiply", ["by"], "COKP", ["int", "int arr"], process.multiply) 
subtract = profile("subtract", ["from"], "CPKO", ["int arr", "int"], process.subtract)
divide = profile("divide", ["by"], "COKP", ["int", "int arr"], process.divide) 
pow = profile("raise", ["to the", "power"], "COKPK", ["int", "str arr"], process.pow)
mod = profile("mod", ["by"], "COKP", ["int", "int"], process.mod)
abs = profile("absolute value of", [], "CO", ["int"], process.absolute_value)
#gcd = profile("greatest common denominator of", [], "CO", ["int arr"], process.greatest_common_denominator)
#square root, circumference, area, volume requires a different liguistic

#LIST
#sort = profile("sort", ["order"], "COKP", ["any arr", "str"], process.sort)
#split = profile("split", ["by"], "COKP", ["str", "str"], process.seperate) #name this split
#join = profile("join", ["with"], "COKP", ["str arr", "str"], process.join)

#VARIABLES
set = profile("set", ["to"], "COKP", ["link"], process.set) 
#see my example function, it inits to the base of that type
create = profile("create", ["as"], "COKP", ["str","str"], process.create) 

#IDE FUNCTIONS
#open_project = profile("open project", [], "CO", ["str"], process.open_project)
#save_project = profile("save project", [], "CO", ["str"], process.save_project)
#run_project = profile("run project", [], "CO", ["str"], process.save_project)
#alter = profile("replace line", ["with"], "CPKO", ["int", "str"], process.change)
#speak = profile("tell me", [], "CO", ["any arr"], process.say)

#LOGIC
_if = profile("if", [], "CO", ["str"], logic_if)
_otherwise = profile("otherwise", [], "C", [], logic_otherwise)
_test = profile("test the value of", [], "CO", ["str"], logic_test)
_when = profile("when", [], "CO", ["str"], logic_when)

#COMPARATOR
_greater = profile("is greater than", [], "PCP", ["int", "int"], greater)
_less = profile("is less than", [], "PCP", ["int", "int"], less)
_greater_or_equal = profile("is greater than or equal to", [], "PCP", ["int", "int"], greater_or_equal)
_less_or_equal = profile("is greater than or equal to", [], "PCP", ["int", "int"], less_or_equal)
_equal = profile("is equal to", [], "PCP", ["int", "int"], equal)


#Don't need LINE function anymore
#SIMPL Processor should be a Library of functions, not a class


profiles = [add, multiply, subtract, divide, pow, mod, abs, 
            set, create, 
            _if, _otherwise, _test, _when,
            _greater, _greater_or_equal, _less, _less_or_equal, _equal]

#current list of commands that work
commands = dict([(f.command, f) for f in profiles])

#--------------------------------Audio Call-----------------------------

input1 = ["Set x to 13",
        "If x is greater than 5",
        "Set x to 10",
        "Otherwise",
        "Set x to 20",
        "Close if"]

input2 = ["Set x to 4",
        "If x is greater than 5",
        "Set x to 10",
        "And if x is less than 2",
        "Set x to 15",
        "Otherwise",
        "Set x to 20",
        "Close if"]

input3 = ["Set x to 5",
        "Set y to 20",
        "Multiply x by y",
        "Raise y to the 7th power"]

input4 = ["Create z as string",
            "If x is greater than 5",
              "If y is greater than 5",
                  "Set x to y",
              "Otherwise",
                  "Set y to x",
              "Close if",
          "Otherwise",
              "If y is less than 50",
                  "Set x to 100",
                  "Set z to hello",
              "Otherwise",
                  "Set y to 200",
              "Close if",
          "Close if"]

input5 = ["Test the value of x",
              "When x is equal to 5",
                  "Set x to 1",
              "When x is equal to 4",
                  "Set x to 2",
              "When x is equal to 3",
                  "Set x to 3",
              "When x is equal to 2",
                  "Set x to 4",
              "When x is equal to 1",
                  "Set x to 5",
          "Close test"]

code = [line.lower() for line in input4]
#****************SUPPORTED*******************
#if         - If x is greater than y
#otherwise  - No Param
#for        - For each x in [1,2,36,7,8]
#while      - While x is less than 100
#until      - Until y is greater than 50
#switch     - test x
#when       - When x is 2
#break      - 
#close      - 


#****************NOT SUPPORTED*******************
#goto
#continue
#call       - 
#begin      - "Start function  
#end        - 
                         
class controlBlock:
    def __init__(self, line, call_cmd):
        #print("init %s %s" % (line, call_cmd))
        self.line = line
        
        #calling command to help parse code
        self.call_cmd = call_cmd
        self.cmd = code[line].split(" ")[0]
        
        #code content
        self.blocks = [[]]
        self.checks = []
        
    def getStruct(self):
        i = self.line
        while(i < len(code)):
            #Get the first word on the line (command or otherwise)
            crnt_cmd = code[i].split(" ")[0]
            
            #print("%s %s %s" % (code[i], i, self.call_cmd))
            
            if(crnt_cmd in ['if', 'for', 'while', 'until', 'test']): #these commands create a subblock
                
                #create a child block
                sub_block = controlBlock(i+1, crnt_cmd)
                sub_block.checks.append(code[i])
                
                #add the child to our code block
                self.blocks[-1].append(sub_block)
                
                #eval the struct of the new block and increase i by the LOC
                i += sub_block.getStruct() + 1
                
            elif (crnt_cmd == 'otherwise'):
                
                #if the parent block is a when block, go back up to the test
                if(self.call_cmd in ['test', 'if']):
                    
                    #create another code block
                    new_block = controlBlock(i+1, crnt_cmd)
                    
                    #add the new block to our block array
                    self.blocks.append([new_block])
                    self.checks.append(code[i])
                    
                    #eval the struct of the new block and increase i by the LOC
                    return i + new_block.getStruct() - self.line + 1 
            
                else:
                    #we need to go back up to the test, return the LOC for our block
                    return i - self.line + 1
            
            elif (crnt_cmd in ['when', 'and']): #these commands split the flow
                
                #if the parent block is a when block, go back up to the test
                if(self.call_cmd in ['test', 'if']):
                    
                    #create another code block
                    new_block = controlBlock(i+1, crnt_cmd)
                    
                    #add the new block to our block array
                    self.blocks.append([new_block])
                    self.checks.append(code[i])
                    
                    #eval the struct of the new block and increase i by the LOC
                    i += new_block.getStruct() 
                else:
                    #we need to go back up to the test, return the LOC for our block
                    return i - self.line + 1
                
            elif (crnt_cmd == 'close'): #close flow
                #if you want to do encapulation, call the close command with the variables to delete
                #self.blocks[-1].append(code[i])
                
                #our function has ended, return the LOC for our block
                return i - self.line + 1
            
            else:
                #if it is not a control flow statement, it's a regular statement
                self.blocks[-1].append(code[i])
                
                #update the row
                i+=1
        return 0
    
        
    def run_program(self, itt, block):
        #if we have a control block
        if(self.call_cmd in ['if', 'for', 'while', 'until', 'when']):                
            i = 0
            while i < len(self.blocks):
                #check the condition of the function
                if(parse(self.checks[i])):
                    self.run_block(itt+1, i)
                    #self.blocks[i].run_program(itt+1, i)
                    return True
                else:
                    i += 1
        else:
            self.run_block(itt, block)
    
    def run_block(self, itt, block):
        #no flow diverting
        for cmd in self.blocks[block]:
            #check if cmd is str or block
            if(isinstance(cmd, controlBlock)):
                #enter block
                cmd.run_program(itt+1, 0)
            else:
                #str cmd
                parse(cmd)
        return
            
    def printStruct(self, itt):     
        for paths in self.blocks:
            for _if in paths:
                if(isinstance(_if, controlBlock)):
                    print(itt*"-->", code[_if.line-1])
                    _if.printStruct(itt+1)
                else:
                    print(itt*"-->", _if)
                
        
        
#run function will call main
#if node.next:
#   run each node.next
#else:
#   run node.code



compiler = controlBlock(0, None)
compiler.getStruct()
compiler.printStruct(0)
print()
print("Main:")
compiler.run_program(1, 0)
print(process.variables)
