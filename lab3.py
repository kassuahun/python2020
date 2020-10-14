#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:24 2020

@author: kassahundegena

Note:
Testing the code is bit time taking specially if you want to test a win case.
it will give you some thing like this 

0  |1 2 3 4 5 6 7 8 9 | 
 ____________________________ 
 1 |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
2  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
3  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
4  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
5  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
6  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
7  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
8  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
9  |◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘ ◘  | 
____________________________
0  |1 2 3 4 5 6 7 8 9 | 
 ____________________________ 
 1 |0 0 0 0 0 1 ☼ 1 0  | 
2  |0 0 0 0 0 1 1 1 0  | 
3  |0 0 0 0 0 1 2 2 1  | 
4  |1 1 0 1 1 2 ☼ ☼ 2  | 
5  |☼ 1 0 1 ☼ 2 3 ☼ 2  | 
6  |1 2 1 2 1 1 1 1 1  | 
7  |0 2 ☼ 2 0 0 0 0 0  | 
8  |0 2 ☼ 2 0 1 1 1 0  | 
9  |0 1 1 1 0 1 ☼ 1 0  | 
For this option you have to uncomment #twoDPrint(maskboard) around line 137. 
It will show you the maskboard to do wining or lose tests several times. 
"""



import random
width = int(input("What is the size in horizontal direction?"))
length = int(input('What is the size in vertical direction?'))
nbombs = int(input('How many mines should we have?'))


board = [['◘']*width for i in range(length)]
maskboard = [[0]*width for i in range(length)]


def twoDPrint(boards):
    i= 0 
    k = 0
    drline ='_'
    print( i  ," |", end = '')
    for line in boards:
        if k>0:
            print(i," |", end="")
        for cars in line:
            if(k == 0): 
                for j in range(len(line)): 
                    print(j+1, "", end="")
                    drline = drline + '___'
                k=2
                i+=1
                print('| \n',drline,'\n',i, "|", end="")
            print(str(cars)[0]+ " ", end="")
        print(' |', '\n', end="")
        i = i+1
    print(drline)

#twoDPrint(board)
#twoDPrint(maskboard)


def numerate( i,j):
    try:
        if i>=0 and j>=0 :
            maskboard[i][j] +=1
    except:
        pass 

def plantBomb():
    #how many bombs width*length * 25%
    #nbombs = int((width*length)/4 )
    
    # Randomly place the bombs
    for i in range(nbombs):
        x = random.randint(0,length-1) 
        y = random.randint(0,width-1)
        maskboard[x][y] ='☼'
    
    #count how many bombs are around a single cell
    for i in range(length):
        for j in range(width): 
            if maskboard[i][j] == '☼': 
                numerate(i-1,j-1)
                numerate(i-1,j)
                numerate(i-1,j+1)
                
                numerate(i,j-1)
                numerate(i,j+1)

                numerate(i+1,j-1)
                numerate(i+1,j)
                numerate(i+1,j+1)
        #twoDPrint(boards)
    return

#expose the indicatr no the player 
def expose(x,y):
    board[x][y]= maskboard[x][y]

#if that coordinate hold bomb.
def isOnBomb(x,y):
    return maskboard[x][y] == '☼'


# if the mask bord and front bord are similar
def isWin():
    win=True

    for i in range(length):
        for j in range(width):
            if maskboard[i][j] == '☼':
                continue
            elif maskboard[i][j] != board[i][j]:
                win=False
                break
    return win


plantBomb()
counter = 0
while True:
    twoDPrint(board)
    twoDPrint(maskboard)
    counter +=1
    print("Enter coordinates separated by space [row col]: or 'exit' to stop ")
    inxy= input()
       
    if inxy=='exit':
      print("OOPS! you lost by Exit")  
      twoDPrint(maskboard)
      break
    else:
        inxy = inxy.split()
        x = int(inxy[0])-1
        y = int(inxy[1])-1
  
    if x>=length or y>=width:
        print('Please incert row between 1 and ' + length)
        print('Please incert Col between 1 and ' + width)
        continue
    
    if isOnBomb(x,y): 
        twoDPrint(maskboard)
        print("OOPS! you lost! You have found [", counter , "] out of [", (width*length)-nbombs , '] Free spaces')
        break
    else:
        expose(x,y)
        if isWin():
            print("Hurra! you won!")
            twoDPrint(maskboard)
            break
