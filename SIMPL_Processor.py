"""
Info:
- Started Wed Mar 27 08:47:24 2019 - Ongoing
- @authors: msabal, tc595, mtapia, kmiller

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

# import SIMPL_Parser as p


class SIMPL_Processor:
    def __init__(self):
        # self.parser = p()
        self.symbols = {
            "comments": {}  # Stores Comments
        }
        self.code = []
        self.current_project = ""
        self.current_line = 0

    def open_project(self, name):
        # Opens Project & Stores Info
        root, ext = os.path.splitext(name)

        # Check If Extension's There
        if not ext:
            ext = ".simpl"
        elif ext != ".simpl":
            print("Invalid project type")
            return -1  # ? Should we have a convention for "invalid" operations

        path = root + ext  # Compose Path

        # Check If File Exists
        if os.path.isfile(path):
            with open(path) as file_in:
                for line in file_in:
                    self.code.append(line.rstrip())
            self.current_project = path
        else:
            print("Project non-existent")
            return -1

    def save_project(self):
        # Saves Project To File
        cp = self.current_project
        if cp == "":
            print("No project opened!")
            return -1
        else:
            file = open(cp, "w")
            for instruction in self.code:
                file.write(f"{instruction}\n")
            file.close()
            print("Successfully saved!")

    def run_project(self):
        # Goes Over Lines, Parser Sends Each Command Here
        for line in self.code:
            self.parser.parse(line)

    def line(self, number):
        # Gives Line Requested By Parser Or Nothing If Non-Existent
        if number > 0 and number <= len(self.code):
            return self.code[number-1]
        else:
            print("Line does not exist")
            return -1

    def change(self, number, command):
        # Changes Instruction At Line
        if number > 0 and number <= len(self.code):
            self.code[number-1] = command
        else:
            return -1

    def create_variable(self, name):
        # Creates An Undefined (None) Variable And Stores It In Symbol H.Table
        if name in self.symbols:  # ? Variable Override. How Should We Handle?
            return -1
        else:
            self.symbols[name] = None

    def create_array(self, name):
        # Creates An Empty Array And Stores It In Symbol H.Table
        self.symbols[name] = []

    def sort(self, name, arr):
        # Sorts Array
        if isinstance(arr, list):
            arr.sort()  # Use Python Built-In Sort (In-Place)
            self.symbols[name] = arr
        else:
            print("Item is not sortable")

    def assign_value(self, name, value):
        # Assigns Value To Symbol (name = string; value = any)
        if name in self.symbols:  # Variable Override
            self.symbols[name] = value
        else:  # Variable Assignment
            self.symbols[name] = value

    def separate(self, name, char):
        # Separates Existing String Variable By Character
        if name in self.symbols:  # Check If Variable Exists
            split_var = self.symbols[name].split(char)  # Split Char
            return split_var
        else:
            print("Variable does not exist")
            return -1

    def comment(self, comment, line):
        # Writes Comment To Symbols - Might Change Imp
        if isinstance(comment, str):
            self.symbols["comments"][line] = comment
        else:
            print("Comment must be a string")
            return -1

    def join(self, name1, name2):
        # Concatenate Two Existing Variables Together
        a_exp = self.symbols[name1] if name1 in self.symbols else False
        b_exp = self.symbols[name2] if name2 in self.symbols else False

        both_valued = a_exp is not False and b_exp is not False

        return f"{a_exp}{b_exp}" if both_valued else -1

    def say(self, target, name):
        # Say The Variable
        if target == 0:
            print(self.symbols[name])
        if target == 1:
            return self.symbols[name]  # Say This Variable

    # Math commands for the processor

    # TODO:

    def add(self, list):
        # Returns the sum/concatenation of all numbers or strings in the list. (list)
        if list[0].isdigit():
            sum = 0
        else:
            sum = ""
        for i in list:
            sum = sum + i
        return sum

    def subtract(self, list):
        # Subtracts numbers in the list. (list)
        dif = list.pop(0)
        for i in list:
            dif = dif - i
        return dif

    def divide(self, list):
        # Returns the division of x by y. (list)
        quo = list.pop(0)
        for i in list:
            quo = quo / i
        return quo

    def multiply(self, list):
        # Returns the multiplication of the list. (list)
        prod = list.pop(0)
        for i in list:
            prod = prod * i
        return prod

    def square_root(self, x):
        # Returns the square root of a number. (int)
        return math.sqrt(x)

    def power(self, x, y):
        # Returns x to the power of y. (int, int)
        return (math.pow(x, y))

    def absolute_value(self, number):
        # Returns distance from zero (int)
        return abs(number)

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

    def greater_than(self, x, y):
        # Returns which value is greater (int, int)
        if x > y:
            return x
        if y > x:
            return y
        else:
            return "They are equal."
    def less_than(self, x, y):
        # Returns which value is least (int, int)
        if x < y:
            return x
        if y < x:
            return y
        else:
            return "They are equal."

    def equal_to(self, list):
        # Determines if the values in the list are equal to one another (list)
        old_num = list.pop(0)
        counter = 0
        for i in list:
            if i != old_num:
                counter = counter + 1
        if counter > 0:
            return false
        else:
            return true






# * Miguel Tests
# main_processor = SIMPL_Processor()  # Creating Instance Of Processor

# main_processor.open_project("./projects/ProcessorTest.simpl")

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
