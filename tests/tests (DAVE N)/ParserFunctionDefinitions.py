# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:47:00 2020

@author: Daniel
"""
from DataType import DataTypes as dtype
from SIMPL_Processor import SIMPL_Processor as processor

TYPE = dtype()
f = processor()

#------------------------------------Function Profiles-------------------------

class profile: 
    def __init__(self, command, keywords, model, parameters, function):
        #class to manage the parsing of specific functions
        self.command = command
        self.keywords = [command] + keywords
        self.model = model
        self.parameters = parameters
        self.function = function
    def _str_(self):
        #for some reason the predefined __str__ was not working
        return self.command, self.keywords, self.model, self.parameters, self.function


#--------------------------------Function Profiles-----------------------------

#each function has specific order and keywords that make it sound natural        
#####################################################################
###                       VARIABLE FUNCTIONS                      ###
#####################################################################
    
#Set x to 5
#Create t as a string
        
var_func = [profile("set", ["to"], "COKP", [TYPE.LINK, TYPE.LINK], f.assign_value),
            profile("create", ["as"], "COKP", [TYPE.STRING, TYPE.STRING], f.create_variable)]

#####################################################################
###                        OUTPUT FUNCTIONS                       ###
#####################################################################

#Say x
#Print x
#Plot x and y

out_func = [profile("say", [], "CO", [], f.say),
            profile("print", [], "CO", [], f.console),
            profile("plot", ["and"], "CPKP", [TYPE.INT_ARR, TYPE.INT_ARR], f.plot)]

#####################################################################
###                         MATH FUNCTIONS                        ###
#####################################################################

#Add 5 to x
#Multiply x by 5
#Subtract 5 from x
#Divide x by 5
#Take the nth root of x
#Raise x to the nth power
#Get the absolute value of x
#get the mean of x
#get the median of x
#get the mode of x
#get the standard deviation of x
#get the variance of x

math_func = [profile("add", ["to"], "CPKO", [TYPE.INT_ARR, TYPE.INT], f.add),
             profile("subtract", ["from"], "CPKO", [TYPE.INT_ARR, TYPE.INT], f.subtract),
             profile("multiply", ["by"], "COKP", [TYPE.INT, TYPE.INT_ARR], f.multiply),
             profile("divide", ["by"], "COKP", [TYPE.INT, TYPE.INT_ARR], f.divide),
             profile("take the", ["root of"], "CPKO", [TYPE.STRING, TYPE.INT], f.root),
             profile("raise", ["to the", "power"], "COKPK", [TYPE.INT, TYPE.STRING], f.pow),
             profile("mod", ["by"], "COKP", [TYPE.INT, TYPE.INT], f.mod),
             profile("get the absolute value of", [], "CO", [TYPE.INT], f.absolute_value),
             profile("get the mean of", ["as"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.mean),
             profile("get the median of", ["as"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.mean),
             profile("get the mode of", ["as"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.mean),
             profile("get the standard deviation of", ["as"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.standard_dev),
             profile("get the variance of", ["as"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.variance)]


#gcd = profile("greatest common denominator of", [], "CO", ["int arr"], processor.greatest_common_denominator)
#circumference, area, volume requires a different liguistic

#Get the area of a {} with sides []
#Get the volume of a {} with sides []


#####################################################################
###                     COMPARATOR FUNCTIONS                      ###
#####################################################################

#x is greater than y
#x is less than y
#x is greater than or equal to y
#x is less than or equal to y
#x is equal to y
#x is inclusively between a and b
#x is exclusively between a and b
#x is inclusively outside a and b
#x is exclusively outside a and b

comp_func = [profile("is greater than", [], "PCP", [TYPE.INT, TYPE.INT], f.greater),
             profile("is less than", [], "PCP", [TYPE.INT, TYPE.INT], f.less),
             profile("is greater than or equal to", [], "PCP", [TYPE.INT, TYPE.INT], f.greater_or_equal),
             profile("is less than or equal to", [], "PCP", [TYPE.INT, TYPE.INT], f.less_or_equal),
             profile("is equal to", [], "PCP", [TYPE.INT, TYPE.INT], f.equal),
             profile("is inclusively between", ["and"], "OCPKP", [TYPE.INT, TYPE.INT, TYPE.INT], f.inclusive_between),
             profile("is exclusively between", ["and"], "OCPKP", [TYPE.INT, TYPE.INT, TYPE.INT], f.exclusive_between),
             profile("is inclusively outside", ["and"], "OCPKP", [TYPE.INT, TYPE.INT, TYPE.INT], f.inclusive_outside),
             profile("is exclusively outside", ["and"], "OCPKP", [TYPE.INT, TYPE.INT, TYPE.INT], f.exclusive_outside)]

#####################################################################
###                         LIST FUNCTIONS                        ###
##################################################################### 

#Sort x ordered ascending/descending
#Split x on commas
#Append 10 to x
#Remove the nth element of x
#Join x to y

list_func = [profile("sort", ["ordered"], "COKP", [TYPE.INT_ARR, TYPE.STRING], f.sort),
             profile("split", ["on"], "COKP", [TYPE.STRING, TYPE.STRING], f.split),
             profile("append", ["to"], "CPKO", [TYPE.LINK, TYPE.LINK_ARR], f.append),
             profile("remove the", ["element from"], "CPKO", [TYPE.STRING, TYPE.ANY_ARR], f.remove),
             profile("join", ["to"], "CPKO", [TYPE.LINK_ARR, TYPE.LINK_ARR], f.join)]
    
#####################################################################
###                          IDE FUNCTIONS                        ###
#####################################################################
#open_project = profile("open project", [], "CO", ["str"], f.open_project)
#save_project = profile("save project", [], "CO", ["str"], f.save_project)
#run_project = profile("run project", [], "CO", ["str"], f.save_project)
#alter = profile("replace line", ["with"], "CPKO", ["int", "str"], f.change)



profiles = var_func + out_func + math_func + comp_func + list_func

#current list of commands that work
commands = dict([(f.command, f) for f in profiles])