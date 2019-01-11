# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:09:01 2019

@author: Lenovo
"""
x = 0
y = 0

def GetInputNo():
    global x
    global y
    x = int(input('Please input first number:'))
    y = int(input('Please input second number:'))

def SumTheVariable(x, y):
    return int(int(x) + int(y))

def OutputResult(x, y, z):
    print('\nThe sum of ' + str(x) + ' and ' + str(y) + ' is ' + str(z) + '.')

GetInputNo()
OutputResult(x, y, SumTheVariable(x, y))

git remote add origin https://github.com/HansonSin/Teacher-Question-Python-3.git
git push -u origin master