"""
Info:
- Started Wed Mar 27 08:47:24 2019 - Ongoing
- @authors: msabal, tc595, mtapia, kmiller, dmarzari
Notes:
- created create_array function
- created comment function
- created sort function
- created separate function
Sources:
- https://stackoverflow.com/questions/3277503/
how-to-read-a-file-line-by-line-into-a-list
"""

import os.path
import math
import decimal
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
from DataType import DataTypes as dtype

TYPE = dtype()


# ADDRESS PRINTS
# ADD TO README

#instance of datatpye class for any casting and data type logic

# ***** Exceptions ***** #
class ProjectError(Exception):
    """Raises Exception For Project Level Errors"""


class ExecutionError(Exception):
    """Raises Exception For Execution Level Errors"""


# ***** Driver Processor ***** #
class SIMPL_Processor:
    # import SIMPL_Parser as p
    # parser = p.Parser()

    def __init__(self):
        # self.parser = p()
        self.symbols = {
            "comments": {},  # Stores Comments
        }
        self.code = []
        self.current_project = ""
        self.current_line = 0

    #####################################################################
    ###                       VARIABLE FUNCTIONS                      ###
    #####################################################################
    
    def create_variable(self, args):
        if args['obj'] in self.symbols: #reject override
            raise ExecutionError("Variable %s Already Exists" % args['obj'])
        else:
            #make a new variable with standard init value for the data type
            type = args['param'][0]
            #we need to clone the list defaults
            if("array" in type):
                self.symbols[args['obj']] = TYPE.init_switch[type][:]
            else:
                self.symbols[args['obj']] = TYPE.init_switch[type]
    
    def assign_value(self, args): #str, any of current var type
        # Assigns Value To Symbol (name = string; value = any)
        val = args['param'][0]
        self.symbols[args['obj']] = val
            
    #####################################################################
    ###                          IDE FUNCTIONS                        ###
    #####################################################################
        
    def open_project(self, name):
        # Opens Project & Stores Info
        root, ext = os.path.splitext(name)

        # Check If Extension's There
        if not ext:
            ext = ".simpl"
        elif ext != ".simpl":
            raise ProjectError("Invalid Project Type")

        path = root + ext  # Compose Path

        # Check If File Exists
        if os.path.isfile(path):
            with open(path) as file_in:
                for line in file_in:
                    self.code.append(line.rstrip())
            self.current_project = path
        else:
            raise ProjectError("Project Non Existent")

    def save_project(self):
        # Saves Project To File
        cp = self.current_project
        if cp == "":
            raise ProjectError("No Project Opened!")
        else:
            file = open(cp, "w")
            for instruction in self.code:
                file.write(f"{instruction}\n")
            file.close()
            print("Successfully saved!")

    def run_project(self):
        # Goes Over Lines, Parser Sends Each Command Here
        # for line in self.code:
        #     self.parser.parse(line)
        return self.code  # Return Bulk Code Array

    def line(self, number):
        # Gives Line Requested By Parser Or Nothing If Non-Existent
        if number > 0 and number <= len(self.code):
            return self.code[number-1]
        else:
            raise ExecutionError("Line does not exist")

    def change(self, number, command):
        # Changes Instruction At Line
        if number > 0 and number <= len(self.code):
            self.code[number-1] = command
        else:
            raise ExecutionError("Line does not exist")

    def comment(self, comment, line):
        # Writes Comment To Symbols - Might Change Imp
        if not len(self.code)-1 < line:
            # Comment Must Be Associated With Existing Line
            raise ExecutionError("Cannot add comment to non-existing line")

        if line in self.symbols["comments"]:
            # Line Already Has A Comment So Add To It
            current_comment = self.symbols["comments"][line]
            self.symbols["comments"][line] = current_comment + comment
        else:
            # Add an entirely new comment
            self.symbols["comments"][line] = comment

    #####################################################################
    ###                        OUTPUT FUNCTIONS                       ###
    #####################################################################
    
    def say(self, args):
        # Say The Variable
        if self.MODE == "SILENT":
            self.console(args)
        else:
            #TODO: Access speach engine, say variable 
            var = args['param'][0]
            print("The value of %s is %s" % (var, self.symbols[var]))  # Say This Variable

    def console(self, args):
        var = args['obj']
        print("%s = %s" % (var, self.symbols[var]))
        #print(self.symbols)
        
    def plot(self, args):
        #plot a series of x coordinates and y coordinates
        #for whatever reason this doens't print to the console right
        xlist = args['param'][0]
        ylist = args['param'][1]
        plt.plot(xlist, ylist)
        plt.show()
        
    #####################################################################
    ###                         MATH FUNCTIONS                        ###
    #####################################################################
    
    def add(self, args): 
        #add [1,2,3] to x
        nlist = args['param'][0]
        self.symbols[args['obj']] += sum(nlist)

    def multiply(self, args):
        #multiply x by [1,2,3]
        nlist = args['param'][0]
        self.symbols[args['obj']] *= int(np.prod(nlist))
        
    def subtract(self, args):
        #subtract [1,2,3] from x
        nlist = args['param'][0]
        self.symbols[args['obj']] -= sum(nlist)
    
    def divide(self, args): 
        #divide x by [1,2,3] 
        nlist = args['param'][0]
        self.symbols[args['obj']] /= int(np.prod(nlist))
    
    def root(self,args):
        #take the nth root of x
        # gets the nth root of x 
        num = int(args['param'][0][:-2])
        self.symbols[args['obj']] **= 1/num
        
    def pow(self,args): #str, str
        #raise x to the nth power
        num = int(args['param'][0][:-2])
        self.symbols[args['obj']] **= num
    
    def mod(self,args): #str, int
        #mod x by n
        num = int(args['param'][0])
        self.symbols[args['obj']] %= num
        
    def absolute_value(self, args):
        #take the absolute value of x
        num = int(args['param'][0])
        self.symbols[args['obj']] = abs(num)

    #####################################################################
    ###                      MATH LIST FUNCTIONS                      ###
    #####################################################################
        
    def mean(self, args):
        # Returns the mean of a list of numbers/variables (list)
        nlist = self.symbols[args['obj']]
        var = args['param'][0]
        self.symbols[var] = np.mean(nlist)

    def median(self, args):
        # Returns the median from a list of numbers (list)
        nlist = self.symbols[args['obj']]
        var = args['param'][0]
        self.symbols[var] = np.median(nlist)
        
    def mode(self, args):
        #Returns the mode and the number of times it is repeated (key, value) from a list of numbers (list)
        nlist = self.symbols[args['obj']]
        var = args['param'][0]
        self.symbols[var] = max(set(nlist), key = nlist.count)
        
    def standard_dev(self, args):
        #Returns the standard deviation of a list
        nlist = self.symbols[args['obj']]
        var = args['param'][0]
        self.symbols[var] = np.std(nlist)
        
    def variance(self, args):
        #Returns the average of squared deviations
        nlist = self.symbols[args['obj']]
        var = args['param'][0]
        self.symbols[var] = np.var(nlist)
        
    #####################################################################
    ###                      GEOMETRIC FUNCTIONS                      ###
    #####################################################################
    
    def circumference(self, radius, uom):
        # Returns circumference of a circle (int, string)
        y = (2 * (math.pi) * radius)
        s = uom
        return "{} {}".format(y, s)

    def area(self, radius, uom):
        # Returns area of a circle (int, string)
        y = (math.pi * radius * radius)
        s = uom
        return "{} {}".format(y, s)

    def greatest_common_denominator(self, x, y):
        # Returns the greatest common divisor of two integers (int, int)
        return math.gcd(x, y)

    def volume(self, shape, uom):
        # Returns the volume of a shape (string, string) input from user = (int), number of variables differ based on shape.
        if shape.lower() == "cube":
            s = input("What is the side length? ")
            r = decimal.Decimal(
                eval(str(decimal.Decimal(s) * decimal.Decimal(s) * decimal.Decimal(s))))
            return "{} {}".format(r, uom)
        if shape.lower() == "parallelepiped":
            s = input("What is the length width and height? ").split(" ")
            r = decimal.Decimal(eval(str(int(s[0]) * int(s[1]) * int(s[2]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "regular prism":
            s = input("What is the base and height? ").split(" ")
            r = decimal.Decimal(eval(str(int(s[0]) * int(s[1]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "cylinder":
            s = input("What is the radius and height? ").split(" ")
            r = decimal.Decimal(
                eval(str(math.pi * (int(s[0]) * int(s[0])) * int(s[1]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "cone" or shape.lower() == "pyramid":
            s = input("What is the base and height? ").split(" ")
            r = decimal.Decimal(eval(str((1 / 3) * int(s[0]) * int(s[1]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "sphere":
            s = input("What is the radius? ")
            r = decimal.Decimal(
                eval(str((4 / 3) * math.pi * (int(s) * int(s) * int(s)))))
            return "{} {}".format(r, uom)
        else:
            print("Shape not included.")
    
    #####################################################################
    ###                     COMPARATOR FUNCTIONS                      ###
    #####################################################################
    
    def greater(self, args):
        #see if element 0 is greater than element 1
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        return elmt0 > elmt1
    
    def greater_or_equal(self, args):
        #see if element 0 is greater than or equal toelement 1
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        return elmt0 >= elmt1
    
    def less(self, args):
        #see if element 0 is less than element 1
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        return elmt0 < elmt1
    
    def less_or_equal(self, args):
        #see if element 0 is less than or equal to element 1
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        return elmt0 <= elmt1
    
    def equal(self, args):
        #see if element 0 is equal to element 1
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        return elmt0 == elmt1
	
    def inclusive_between(self, args):
        #see if element 0 is between element 1 and element 2 (where element 1 < element 2)
        obj = self.symbols[args['obj']]
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        if(elmt0 < elmt1):
            return ((obj >= elmt0) and (obj <= elmt1))
	
    def exclusive_between(self, args):
        #see if element 0 is between element 1 and element 2 (where element 1 < element 2)
        obj = self.symbols[args['obj']]
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        if(elmt0 < elmt1):
            return ((obj > elmt0) and (obj < elmt1))
        
    def inclusive_outside(self, args):
        #see if element 0 is < element 1 or > element 2 (where element 1 < element 2)
        obj = self.symbols[args['obj']]
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        if(elmt0 < elmt1):
            return ((obj <= elmt0) or (obj >= elmt1))
	
    def exclusive_outside(self, args):
        #see if element 0 is < element 1 or > element 2 (where element 1 < element 2)
        obj = self.symbols[args['obj']]
        elmt0 = args['param'][0]
        elmt1 = args['param'][1]
        if(elmt0 < elmt1):
            return ((obj < elmt0) or (obj > elmt1))
    
    #####################################################################
    ###                         LIST FUNCTIONS                        ###
    ##################################################################### 
            
    def join(self, args):
        #Join two lists together
        self.symbols[args['obj']] += args['param'][0]
    
    def split(self, args): 
        # Splits Existing String Variable By Character/string
        keyword_switch = {"commas" : ",", 
                          "periods" : "."}
        text = args['param'][0]
        char = args['param'][1]
        
        #if the split char/string is a keword, get the character equivalent
        if(char in keyword_switch.keys()):
            char = keyword_switch[char]
        
        self.symbols[args['obj']] = text.split(char)    
    
    def append(self, args):        
        #add element to list
        element = args['param'][0]
        self.symbols[args['obj']].append(element)

    def remove(self, args):
        #remove element from the list by index ('1st', '2nd', '3rd' => 0, 1, 2)
        index = int(args['param'][0][:-2])-1
        self.symbols[args['obj']].pop(index)
    
    def sort(self, args):
        # Use Python Built-In Sort (In-Place)
        direction = args['param'][0]
        if(direction == "ascending"):
            self.symbols[args['obj']].sort()
        if(direction == "descending"):
            self.symbols[args['obj']].sort(reverse=True)

    
    
    
    
# * Miguel Tests
# main_processor = SIMPL_Processor()  # Creating Instance Of Processor

# main_processor.open_project("./projects/hi.txt")

# main_processor.comment("This is a comment", 5)
# main_processor.assign_value("Programmer", "Miguel Tapia")
# main_processor.comment("Something else", 2)


# print(main_processor.symbols)

# print(main_processor.code)
# print(f"Find Line Cmd: {main_processor.line(1)}")
# main_processor.change(1, "cheese")
# main_processor.save_project()
# print(main_processor.code)

# print(main_processor.add(100, 20))

# * Ken Tests
#main_processor = SIMPL_Processor()  # Creating Instance Of Processor

#print(main_processor.mode([1,1,2,2,3])
