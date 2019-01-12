# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 01:40:38 2019

@author: liting
"""

x = 0
y = 0

def GetInputNo():
    global x # why you need a global variable? 
    global y
    x = int(input('Please input first number:'))
    y = int(input('Please input second number:'))

def SumTheVariable(x, y):
    return int(int(x) + int(y)) # int(x) + int(y) should be datatype integer, why you need to cast to int?

def OutputResult(x, y, z):
    print('\nThe sum of ' + str(x) + ' and ' + str(y) + ' is ' + str(z) + '.')
    # you can also do the printing as the code below
GetInputNo()
OutputResult(x, y, SumTheVariable(x, y))


##### OR You may do like this
def GetInputNo():
    x = int(input('Please input first number:'))
    y = int(input('Please input second number:'))
    return x, y

def SumTheVariable(x, y):
    return int(x) + int(y)

def OutputResult(x, y, z):
    print('\nThe sum of %d and %d is %d.' %( x, y, z))

x, y = GetInputNo()
OutputResult(x, y, SumTheVariable(x, y))
