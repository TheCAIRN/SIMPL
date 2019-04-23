# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:47:24 2019

@author: msabal
"""
class SIMPL_Processor:
    import TheActualOne as p
    parser = p.Parser()
    
    def __init__(self):
        self.symbols = {}
        self.code = []
        self.current_project = ""
        self.current_line = 0
    
    def open_project(self,name):
        # Open a project file and store the results in self.code
        self.current_project = name
    
    def save_project(self,name):
        return
    
    def run_project(self):
        for line in self.code:
            parser.parse(line)
    
    def line(self,number):
        if number >= 0 and number < self.code.count:
            return self.code[number]
        else:
            return ""
        
    def change(self,number,command):
        self.code[number] = command
    
    def create_variable(self,name):
        #insert string into symbols
        str = ""
        self.symbols[name] = str
        
        return
    
    def create_array(self,name):
        return
    
    def sort(self,name):
        return
    
    def assign_value(self,name,value):
        self.symbols[name] = value
        return
    
    def separate(self,name,value):
        return
    
    def comment(self,comment):
        return
    
    def join(self,name1,name2):
        return self.symbols[name1] + " " + self.symbols[name2]
    
    def say(self,target,name):
        # If target = 0, print to console
        # If target = 1, call the text-to-speech engine
        if target == 0:
            print(self.symbols[name])
        if target == 1:
            # To do
            
    
    
    
    
    