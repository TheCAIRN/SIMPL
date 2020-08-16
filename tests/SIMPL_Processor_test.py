import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from SIMPL_Processor import SIMPL_Processor


class Test_Assign_Value(unittest.TestCase):
    def setUp(self):
        self.processor = SIMPL_Processor()
        self.processor.open_project("./projects/TestOne")

    def test_assign_value(self):
        self.processor.assign_value("Programmer", "Miguel Tapia")
        self.assertEqual(self.processor.symbols["Programmer"], "Miguel Tapia")


class Test_Line_Return(unittest.TestCase):
    def setUp(self):
        self.processor = SIMPL_Processor()
        self.processor.open_project("./projects/TestOne")

    def test_line(self):
        line_command = self.processor.code[16]
        self.assertEqual(line_command, "RUN PROJECT")


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Test_Assign_Value))
    test_suite.addTest(unittest.makeSuite(Test_Line_Return))
    return test_suite


test_suite = suite()
runner = unittest.TextTestRunner()
runner.run(test_suite)


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
