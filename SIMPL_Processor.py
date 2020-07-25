"""
Info:
- Started Wed Mar 27 08:47:24 2019 - Ongoing
- @authors: msabal, tc595, mtapia

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
# import SIMPL_Parser as p


class SIMPL_Processor:
    def __init__(self):
        # self.parser = p.Parser()
        self.symbols = {}
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
            return

        path = root + ext  # Compose Path

        # Check If File Exists
        if os.path.isfile(path):
            with open(path) as file_in:
                for line in file_in:
                    self.code.append(line.rstrip())
            self.current_project = path
        else:
            print("Project non-existent")

    def save_project(self):
        # Saves Project To File
        cp = self.current_project
        if (cp == ""):
            print("No project opened!")
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
            return ""

    def change(self, number, command):
        # Changes Instruction At Line
        self.code[number-1] = command

    def create_variable(self, name):
        # TODO: insert string into symbols
        str = ""
        self.symbols[name] = str

        return

    def create_array(self, name):
        # TODO: insert array into symbols
        arr = []

        # create array
        for name in arr:
            self.symbols.append(name)

        return

    def sort(self, name, arr):
        # TODO: Sort
        length = len(arr)

        for i in range(length):
            for j in range(0, length - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        self.symbols[name] = arr

        return

    def assign_value(self, name, value):
        # TODO: Assign Values
        self.symbols[name] = value
        return

    def separate(self, name, value):
        # TODO: Separate
        str = ""
        for value in str:
            str.split(value)

        self.symbols[name] = str

        return

    def comment(self, comment):
        # TODO: insert comment into symbols
        # comment = ""

        # create comment
        # self.symbols[name] = "#" + comment

        return

    def join(self, name1, name2):
        # TODO: Join
        return self.symbols[name1] + " " + self.symbols[name2]

    def say(self, target, name):
        # TODO: Say
        # If target = 0, print to console
        # If target = 1, call the text-to-speech engine
        if target == 0:
            print(self.symbols[name])
        if target == 1:
            # To do
            return
        
    #Math commands start
    import math
    import decimal

    def absolute_value(number):
        return abs(number)

    def circumference(radius, uom):
        y = (2*(math.pi)*radius)
        s = uom
        return "{} {}".format(y, s)

    def area(radius, uom):
        y = (math.pi*radius*radius)
        s = uom
        return "{} {}".format(y, s)

    def greatest_common_denominator(x, y):
        return math.gcd(x, y)

    def volume(shape, uom):
        if shape.lower() == "cube":
            s = input("What is the side length? ")
            r = decimal.Decimal(eval(str(decimal.Decimal(s) * decimal.Decimal(s) * decimal.Decimal(s))))
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
            r = decimal.Decimal(eval(str(math.pi * (int(s[0]) * int(s[0])) * int(s[1]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "cone" or shape.lower() == "pyramid":
            s = input("What is the base and height? ").split(" ")
            r = decimal.Decimal(eval(str((1/3) * int(s[0]) * int(s[1]))))
            return "{} {}".format(r, uom)
        if shape.lower() == "sphere":
            s = input("What is the radius? ")
            r = decimal.Decimal(eval(str((4/3) * math.pi * (int(s) * int(s) * int(s)))))
            return "{} {}".format(r, uom)
        else:
            print("Shape not included.")


main_processor = SIMPL_Processor()

main_processor.open_project("./projects/ProcessorTest.simpl")

print(main_processor.code)
print(f"Find Line Cmd: {main_processor.line(1)}")
main_processor.change(0, "other")
main_processor.save_project()
print(main_processor.code)
