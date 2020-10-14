#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:24 2020

@author: kassahundegena

Note:
This is for lab 2 Task 2
"""


a = open("python.txt","rt") #opening file.
wordList = {}
lines = a.readlines() #read all lines once and return list hold each line as elemet
#print(lines)
for line in lines:
    # comma, full stop, newline, quotation marks, apostrophe. 
    line = line.replace('\n', '')
    line = line.replace(',', '')
    line = line.replace('.', '')
    line = line.replace('"', '')
    line = line.replace("'","")
    words = line.split()
    #print(words)

    for word in words:
        if word in wordList:
            wordList[word] += 1
        else:
            wordList[word] = 1

for target_list in wordList:
    if wordList[target_list] > 3:
        print (target_list + ":" + str(wordList[target_list]))


a.close()