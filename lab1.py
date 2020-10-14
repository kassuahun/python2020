#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:24 2020

@author: kassahundegena

Note:
All Tasks are in one file, runn one by one.
"""
print ("Task 1")
print ("What is your name? ")
name = input()
print ("How many cookies would you like to have ?")
cookies = int(input())
for i in range(cookies):
    print ("cookies", end=' ') 



print("Task 2")

print ("What is your name? ")
name = input()
print ("How many cookies would you like to have ?")
cookies = int(input())

if cookies < 10:
    print("Are you sure it’s enough?")
    
elif cookies < 20:
    print("I agree cookies are delicious! ")
elif cookies < 51:
    print ("Be careful, it’s getting too much")
elif cookies > 50:
    print ("No way, it’s getting too much")
    cookies = 50
else:
    print("Something must be wrong, I give you 10 cookies")
    cookies = 10

for i in range(cookies):
    print ("cookies", end=' ') 


print("Task 3")
print("Howmany no do you have?")
size = int(input())
numsList = []
for i in range(1,size+1):
    print("what is the " + str(i) + ". number")
    numsList.append(int(input()))
    

sum = 0
for x in numsList:
    sum = sum + int(x)
avarage = sum/len(numsList)
print ("the avarage is " + str(round(avarage,2)))