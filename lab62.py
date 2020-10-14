#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:41:58 2020
Lab 6.
Topic: Object Oriented Programming

@author: kassahundegena
"""

class Course_grade:
    
    #Class constructor
    def __init__(self):
        self.normalAssignments=[]
        self.gradedAssignments = []
        self.finalExam=''
        self.examWeight = ''
        self.gradedAssigWeight = []
    
    
    #Set the result of one assignment 
    def set_assignment(self, index, grade):
        self.normalAssignments[index] = grade

    #Set the result of all assignments at once 
    def set_assignments(self, gradelist):
        self.normalAssignments = gradelist
    
    #Set the result of one graded assignment 
    def set_graded_assignment(self, index, grade):
        self.gradedAssignments[index] = grade
    
    #Set the results of all graded assignments at once 
    def set_graded_assignments(self, gradelist):
        self.gradedAssignments = gradelist
    
    #Set the result of the final exam 
    def set_exam(self, score):
        self.finalExam = score
    #    
    def get_grade(self):
        finalgrade = ''
        assignmentgrade = 0
        for i in range(len(self.gradedAssigWeight)):
            assignmentgrade = assignmentgrade + self.gradedAssignments[i] * self.gradedAssigWeight[i]/100
        
        finalgrade= self.finalExam*self.examWeight/100 + assignmentgrade
        
       #If an assignment was not submitted then the final grade is F 
        if False in self.normalAssignments:
            finalgrade = 'F'
        #Graded assignment has to be at least 40 of final grade.
        elif len(self.gradedAssigWeight)>0 and assignmentgrade/finalgrade < 0.4:
            finalgrade = 'F'
       
        #Final exam has to be at least 40 of final grade.
        elif self.finalExam/finalgrade < 0.4:
            finalgrade = 'F'
        
        #cases after preconditions fulfilled.
        #(<40% F, >=40 and <50 E, >=50 and <60 D, >=60 and <80 C, >=80 and <90 B, >=90 and <=100 A) 
        
        elif finalgrade < 40:
            finalgrade = 'F'
        elif 40 <= finalgrade < 50:
            finalgrade = 'E'
        elif 50 <= finalgrade < 60:
            finalgrade = 'D'
        elif 60 <= finalgrade < 80:
            finalgrade = 'C'
        elif 80 <= finalgrade < 90:
            finalgrade = 'B'
        elif 90 <= finalgrade <= 100:
            finalgrade = 'A'
       
        return finalgrade
    #  assignments calculated according to given weight   
   
    
    #final grade will be exam*weightpersentage plus assignments. 
    #assignment will be 0 if there is no graded assignment.
    
        
    #I have added this class to debug easly, it print the contents 
    def display(self):
        print("normalAssignments = ", self.normalAssignments)
        print("gradedAssignments =", self.gradedAssignments)
        print('finalExam =' , self.finalExam)
        print('examWeight = ', self.examWeight)
        print('gradedAssigWeight =' ,self.gradedAssigWeight)  
        
#child class which inherited Course_grade
class ACIT4420_2020(Course_grade):
    def __init__(self):
        self.normalAssignments=[]
        self.gradedAssignments = []
        self.finalExam=''
        self.examWeight = 50
        self.gradedAssigWeight = [5,7,10,6,7,8,7]

#child class which inherited Course_grade
class ACIT4420_2019(Course_grade):
    def __init__(self):
         self.normalAssignments=[0,0,0,0,0,0,0]
         self.gradedAssignments = []
         self.finalExam=''
         self.examWeight = 100
         self.gradedAssigWeight = []
        
#Given cases as per assignment text
a = ACIT4420_2020()
a.set_graded_assignments([70,70,70,70,70,70,70])
a.set_graded_assignment(2,100)
a.set_exam(76) 
a.display()
print(a.get_grade())

a2 = ACIT4420_2019()
a2.set_assignments([True,True,True,True,True,True,True])
a2.set_exam(76) 
a2.display()
print(a2.get_grade())

b = ACIT4420_2020()
b.set_graded_assignments([20,20,20,20,20,20,20])
b.set_graded_assignment(2,100)
b.set_exam(84)
b.display()
print(b.get_grade()) 

b2 = ACIT4420_2019()
b2.set_assignments([True,True,True,True,True,True,True])
b2.set_exam(84)
b2.display()
print(b2.get_grade()) 





