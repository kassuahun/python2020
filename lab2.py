#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:24 2020

@author: kassahundegena

Note:
This is for Task 1.
"""

#Use a tuple to understand the days (Monday, Tuesday, ..) and use one list to store the programs. 
days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
hrs = (0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)
programList = []

for day in days:
    temp = []  
    for hr in hrs:
        temp.append([str(hr)+":00", ''])
    programList.append(temp)
#{"Monday":{}},"Tuesday":{},"Wednesday":{},"Thursday":{},"Friday":{},"Saturday":{},"Sunday":{})

def menu():
    print(''' 
            s - Store program
            l - List daily program
            x - Exit
            ''')
def printCalander(in_List):
    for target in in_List:
        print(target[0] + " " + target[1])

def storeProgram():
    program = []
    print("Which day?")
    index = days.index(input())
    program = programList[index]

    #program.append(input())
    print("What time?")
    time = int(input())
    print("What is the program?")
    program[time][1]= input()

def listProgram():
    print("which day?: ")
    choose = input()
    if choose in days:
        printCalander(programList[days.index(choose)])
    else:
        print ("Unknown day")
    return None


while True:
    menu()
    print("Choose from the list: ")
    choose= input()
    if choose=='s':
        storeProgram()
    elif choose == 'l':
        listProgram()
    elif choose == 'x':
        break
    else:
        print("Unknown choise")
print("done")





