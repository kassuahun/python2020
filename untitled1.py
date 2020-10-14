#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:24 2020

@author: kassahundegena
"""
# regular expression expressions 
import re  
  
# Example string  
f = open("canvas.txt", "r")
t = f.read(-1)

lst1 = re.findall('[s][0-9]+@oslomet.no', t) 

lst2 = re.findall('[-+.0-9A-Z_a-z]+@[-+.0-9_a-z]+\.[A-Za-z]{2,4}', t)
#lst3 = re.findall('[-+0-9]{1,2}\s[-+A-Za-z]{3}\s[A-Za-z]{2}\s[-+0-9]{1,2}:[-+0-9]{1,2}', t)
lst3 = re.findall('[-+0-9]{1,2}\s[-+A-Za-z]{3}\sat\s[-+0-9]{1,2}:[-+0-9]{1,2}', t)
#lst4 = \sfs:[-+0-9]{3}:[-+0-9]{6,7}

lst4= re.findall('fs:[-+0-9]{3}:[-+0-9]{6,7}',t)

lst5=re.findall('[-+0-9]{2}:[-+0-9]{2}:[-+0-9]{2}', t)

lst6 = re.findall('/^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n/m', t)

#lst6 = re.findall('^([A-Za-z-æåø]+)\s([A-Za-z-]+)\n|^([A-Za-z]+)\s([A-Za-z]+)\s([A-Za-z-]+)\n|^([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\n|^([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\n', t)
regex = (r"^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n\n")
lst7=re.findall("^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n\n", t, re.MULTILINE)
'''
matches = re.finditer(regex, t, re.MULTILINE)
for matchNum, match in enumerate(matches, start=1):
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

  
# Printing of List  '[-+.0-9A-Z_a-z]+@[-+.0-9_a-z]+\.[A-Za-z]{2,4}', 'fs:[-+0-9]{3}:[-+0-9]{6,7}'
#\S+@[[a-z0-9]+[.]+[a-z]{2,3}
#[-+.0-9A-Z_a-z]+@[-+.0-9_a-z]+\.[A-Za-z]{2,4}
[-+.0-9A-Z_a-z]+@[-+.0-9_a-z]+\.[A-Za-z]{2,4}\sfs:[-+0-9]{3}:[-+0-9]{6,7}

^([A-Za-z-æåø]+)\s([A-Za-z-]+)\n|^([A-Za-z]+)\s([A-Za-z]+)\s([A-Za-z-]+)\n|^([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\n|^([A-Za-z-]+)\s([A-Za-z-]+)\s([A-Za-z]+)\s([A-Za-z-]+)\s([A-Za-z-]+)\n

(^([A-Za-z-æåø^\n]+\s){2,5})
^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n|^[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-zæåø]+\s[A-Z-ÅØÆa-z-æåø]+\s[A-Z-ÅØÆa-z-æåø]+\n


(ACIT4420-1 20H)\n(Student)\n(\d\d\s[A-Z][a-z]+\sat\s\d\d:\d\d)\n(\d\d:\d\d:\d\d)
\s(s\d\d\d\d\d\d@oslomet.no)\s(fs:[0-9]{3}:[0-9]{6,7})\s\n(ACIT4420-1 20H)\n(Student)\n(\d\d\s[A-Z][a-z]+\sat\s\d\d:\d\d)\n(\d\d:\d\d:\d\d)
(\d\d:\d\d:\d\d)\n(.+)\n(.+)\s(s\d\d\d\d\d\d@oslomet.no)\s(fs:[0-9]{3}:[0-9]{6,7})\s\n(ACIT4420-1 20H)\n(\w+)\n(\d\d\s[A-Z][a-z]+\sat\s\d\d:\d\d)\n(\d\d:\d\d:\d\d)
'''
print(lst1) 
print(lst2) 
print(lst3) 
print(lst4) 
print(lst5)
print(lst7)
