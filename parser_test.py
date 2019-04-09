# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:59:48 2019

@author: sw344
"""

import TheActualOne as p
parser = p.Parser()
parser.parse("Create Variable Hello")
parser.parse("Create Variable World")
#Ty will need to change assign to set see the commands file on github
parser.parse("Set Hello To Hello")
parser.parse("Set World to World")

parser.parse("Join Hello To World")

parser.parse("Run Project")