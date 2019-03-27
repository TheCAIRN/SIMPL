# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:47:24 2019

@author: msabal
"""

class SIMPL_Processor:
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
        return
    def line(self,number):
        if number >= 0 and number < self.code.count:
            return self.code[number]
        else:
            return ""
    def create_variable(self,name):
        return
    def create_array(self,name):
        return
    def sort(self,name):
        return
    def assign_value(self,name):
        return
    def separate(self,name,value):
        return
    def comment(self,comment):
        return
    def join(self,name1,name2):
        return