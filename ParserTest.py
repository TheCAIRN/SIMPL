# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:02:34 2019

@author: msabal
"""

import TheActualOne as p
parser = p.Parser()
filename = "TestOne.SIMPL"
fp = open(filename,"r")
for line in fp:
    p.input(line)