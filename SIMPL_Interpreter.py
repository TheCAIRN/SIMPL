# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:49:11 2020

@author: Daniel


"""
import SIMPL_Processor as process

#------------------------------------------Definitions-------------------------
class profile:
    def __init__(self, command, keywords, model, parameters, call):
        #class to manage the parsing of specific functions
        self.command = command
        self.keywords = keywords
        self.model = model
        self.parameters = parameters
        self.call = call

    def run(self, vars):
        #type checking here
        print(vars)
        if(self.model.find("O") < self.model.find("P")): #object comes first
            obj = vars[0]
            
            if(self.parameters[1] == "any"):
                #this need to be a more robust solution
                param = type_check(vars[1], str(type(process.variables[obj])).split("'")[1])
            else:
                param = type_check(vars[1], self.parameters[1])
        else: #parameters come first
            obj = vars[1]
            param = type_check(vars[0], self.parameters[0])
        
        #print(obj, param)
        self.call(obj, param)
        print(process.variables)

#--------------------------------Casting--------------------------------
def type_check(var, vtype):
    #print("cast %s %s" % (var, vtype))
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
          "any arr" : t_any_arr
          }

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
gcd = profile("greatest common denominator of", [], "CO", ["int arr"], process.greatest_common_denominator)
#square root, circumference, area, volume requires a different liguistic

#LIST
sort = profile("sort", ["order"], "COKP", ["any arr", "str"], process.sort)
split = profile("split", ["by"], "COKP", ["str", "str"], process.seperate) #name this split
join = profile("join", ["with"], "COKP", ["str arr", "str"], process.join)

#VARIABLES
set = profile("set", ["to"], "COKP", ["any","any"], process.set) 
#see my example function, it inits to the base of that type
create = profile("create", ["as"], "COKP", ["str","str"], process.create_variable) 

#IDE FUNCTIONS
open_project = profile("open project", [], "CO", ["str"], process.open_project)
save_project = profile("save project", [], "CO", ["str"], process.save_project)
run_project = profile("run project", [], "CO", ["str"], process.save_project)
alter = profile("replace line", ["with"], "CPKO", ["int", "str"], process.change)
speak = profile("tell me", [], "CO", ["any arr"], process.say)

#LOGIC
#different linguistic. More next week


#Don't need LINE function anymore
#SIMPL Processor should be a Library of functions, not a class


profiles = [add, multiply, subtract, divide, pow, mod, set, create]

#current list of commands that work
commands = dict([(f.command, f) for f in profiles])

