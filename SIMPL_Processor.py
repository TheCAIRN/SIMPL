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
# import TheActualParser as p


class SIMPL_Processor:
    def __init__(self):
        # self.parser = p.Parser()
        self.symbols = {}
        self.code = []
        self.current_project = ""
        self.current_line = 0

    def open_project(self, name):
        root, ext = os.path.splitext(name)

        if not ext:
            ext = ".simpl"
        elif ext != ".simpl":
            print("Invalid project type")
            return

        path = root + ext

        # Opens Project & Stores Info
        if os.path.isfile(path):
            with open(path) as file_in:
                for line in file_in:
                    self.code.append(line.rstrip())
            self.current_project = path.replace(".simpl", "")
        else:
            print("Project non-existent")

    def save_project(self, name):
        # Saves Project To File
        return

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
        self.code[number] = command

    def create_variable(self, name):
        # insert string into symbols
        str = ""
        self.symbols[name] = str

        return

    def create_array(self, name):
        # insert array into symbols
        arr = []

        # create array
        for name in arr:
            self.symbols.append(name)

        return

    def sort(self, name, arr):
        length = len(arr)

        for i in range(length):
            for j in range(0, length - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        self.symbols[name] = arr

        return

    def assign_value(self, name, value):
        self.symbols[name] = value
        return

    def separate(self, name, value):
        str = ""
        for value in str:
            str.split(value)

        self.symbols[name] = str

        return

    def comment(self, comment):
        # insert comment into symbols
        # comment = ""

        # create comment
        # self.symbols[name] = "#" + comment

        return

    def join(self, name1, name2):
        return self.symbols[name1] + " " + self.symbols[name2]

    def say(self, target, name):
        # If target = 0, print to console
        # If target = 1, call the text-to-speech engine
        if target == 0:
            print(self.symbols[name])
        if target == 1:
            # To do
            return


main_processor = SIMPL_Processor()

main_processor.open_project("ProcessorTest.simpl")

print(f"Find Line Cmd: {main_processor.line(1)}")
