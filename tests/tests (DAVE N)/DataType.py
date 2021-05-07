# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:35:41 2020

@author: Daniel
"""

class DataTypes:
    VARCONN = None
    
    #enums
    ANY = 0
    LINK = 1
    BOOLEAN = 2
    INT = 3
    FLOAT = 4
    STRING = 5
    ANY_ARR = 6
    LINK_ARR = 7
    BOOLEAN_ARR = 8
    INT_ARR = 9
    FLOAT_ARR = 10
    STRING_ARR = 11
    
    #init values for these variables
    init_switch = {'a boolean': False,
                   'an integer': 0,
                   'a float': 0.9,
                   'a string arrray': "",
                   'a boolean array': [False],
                   'an integer array': [0],
                   'a float array': [0.0],
                   'a string array': [""]}
    
    def __init__(self):
        self.type_switch = {2  : self.toBOOL,
                            3  : self.toINT,
                            4  : self.toFLOAT,
                            5  : self.toSTRING}
    
    def get_type(self, val):
        #get class of variable
        vtype = str(type(val))
        if('bool' in vtype):
            return self.BOOLEAN
        if('int' in vtype):
            return self.INT
        if('float' in vtype):
            return self.FLOAT
        if('str' in vtype):
            return self.STRING
        
        if('list' in vtype):
            #anything over is a 2D array (doesn't support casting)
            return self.get_type(val[0]) + 6

    def cast(self, str_in, ctype, lvar):
        #string input, cast type, link variable (if applicable)
        #print("Cast %s to %s link %s" % (str_in, ctype % 6 == 1, lvar))
        
        #if the object isn't None and the type is a link we need to find the type of the variable
        if((lvar != None) and (ctype % 6 == 1)):
            ctype = self.get_type(lvar)
        
        #if its a list, lets cast each component individually
        if(ctype >= 6):
            out = []
            #itterate over each element
            for elmt in str_in.split(" "):
                #if the element is a variable take it from the symbols, otherwise cast it
                if(elmt in self.VARCONN):
                    out.append(self.VARCONN[elmt])
                else:
                    out.append(self.type_switch[ctype-6](elmt))
        else:
            #if the string is a variable name, get the value, otherwise cast it
            if(str_in in self.VARCONN):
                out = self.VARCONN[str_in]
            else:
                out = self.type_switch[ctype](str_in)
            
        
        if(out != None):
            return out
        else:
            raise Exception("Could not cast %s to %s" % (str_in, ctype))
    
    def toBOOL(self, str_in):
        if(str_in == "true"):
            return True
        elif(str_in == "false"):
            return False
            
    def toINT(self, str_in):
        if(str_in.replace('-', '').isdigit()):
            return int(str_in)
    
    def toFLOAT(self, str_in):
        if(str_in.replace('-', '').replace('.', '').isdigit()):
            return float(str_in)
    
    def toSTRING(self, str_in):
        #this is a waste
        return str_in