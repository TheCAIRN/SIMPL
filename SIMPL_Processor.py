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
        # self.parser = p()
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
        # Assigns Value To Symbol
        if name in self.symbols:  # Variable Override
            self.symbols[name] = value
        else:  # Variable Assignment
            self.symbols[name] = value

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
        # Concatenate Two Variables Together
        a_exp = self.symbols[name1] if name1 in self.symbols else False
        b_exp = self.symbols[name2] if name2 in self.symbols else False

        both_valued = a_exp is not False and b_exp is not False

        return f"{a_exp}{b_exp}" if both_valued else -1

    def say(self, target, name):
        # TODO: Say
        # If target = 0, print to console
        # If target = 1, call the text-to-speech engine
        if target == 0:
            print(self.symbols[name])
        if target == 1:
            # To do
            return


# main_processor = SIMPL_Processor()

# main_processor.open_project("./projects/ProcessorTest.simpl")

# print(main_processor.code)
# print(f"Find Line Cmd: {main_processor.line(1)}")
# main_processor.change(0, "other")
# main_processor.save_project()
# print(main_processor.code)
