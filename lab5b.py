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
test_str = f.read(-1)

regex = r"\b(.+)\n(.+)\s([-+.0-9A-Z_a-z]+@[-+.0-9_a-z]+\.[A-Za-z]{2,4})\s(fs:[0-9]{3}:[0-9]{6,7})\t\n(ACIT4420-1 20H)\n(\w+)\n([-+0-9]{1,2}\s[-+A-Za-z]{3}\sat\s[-+0-9]{1,2}:[-+0-9]{1,2})\n([-+0-9]{1,2}:[-+0-9]{1,2}:[-+0-9]{1,2})\b"

matches = re.finditer(regex, test_str, re.MULTILINE)
question1=[] # oslomet emails
question2=[] #any email 
question3=[] #last activity eg 13 Sep at 16:57
question4=[]    #sys ID fs:215:1032851
question5=[]    #Tottal activity time 07:59:54
question6=[]    #name of student ...
question7=[]    #students active more than 10hr
question8=[]    #students last log in Augest

for matchNum, match in enumerate(matches, start=1):
    
    #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    if (re.search('[s][0-9]+@oslomet.no', match.group(3))):
        question1.append(match.group(3))
    
    question2.append(match.group(3))
    question3.append(match.group(7))
    question4.append(match.group(4))
    question5.append(match.group(8))    
    question6.append(match.group(2))
    if(re.search('^[1-9]', match.group(8))):
       question7.append(match.group(2))
       
    if(re.search(' Aug ', match.group(7))):
       question8.append(match.group(2))
    
    
print(question1) # oslomet emails
print(question2) #any email 
print(question3) #last activity eg 13 Sep at 16:57
print(question4) #sys ID fs:215:1032851
print(question5) #Tottal activity time 07:59:54
print(question6) #name of student ...
print(question7) #students active more than 10hr
print(question8) #students last log in Augest

print('Tests')

oslometemail= ['s351656@oslomet.no', 's356528@oslomet.no', 's350141@oslomet.no', 's326326@oslomet.no', 's341354@oslomet.no', 's341358@oslomet.no', 's309854@oslomet.no', 's341474@oslomet.no', 's349771@oslomet.no', 's326609@oslomet.no', 's326151@oslomet.no', 's348572@oslomet.no', 's236646@oslomet.no', 's188110@oslomet.no', 's329926@oslomet.no', 's171212@oslomet.no', 's325909@oslomet.no', 's319478@oslomet.no', 's341460@oslomet.no', 's166126@oslomet.no', 's339971@oslomet.no', 's356469@oslomet.no', 's325920@oslomet.no', 's198759@oslomet.no', 'laszloer@oslomet.no', 's346664@oslomet.no', 's182417@oslomet.no', 's310338@oslomet.no', 's235401@oslomet.no', 's321045@oslomet.no', 's350110@oslomet.no', 's173307@oslomet.no', 's348002@oslomet.no', 's356066@oslomet.no', 's348588@oslomet.no', 'tomglove@oslomet.no', 's319482@oslomet.no', 's234031@oslomet.no', 's349473@oslomet.no', 's341467@oslomet.no', 's315740@oslomet.no', 'solvorho@oslomet.no', 's349009@oslomet.no', 's356550@oslomet.no', 's351659@oslomet.no', 's340018@oslomet.no', 's351646@oslomet.no', 's331043@oslomet.no', 's310455@oslomet.no', 's314769@oslomet.no', 's336602@oslomet.no', 's351645@oslomet.no', 's319470@oslomet.no', 's319496@oslomet.no', 's345532@oslomet.no', 's108343@oslomet.no', 's315310@oslomet.no', 's169909@oslomet.no', 's326178@oslomet.no', 's325936@oslomet.no', 's150048@oslomet.no', 's351653@oslomet.no', 's309855@oslomet.no', 's326166@oslomet.no', 's351654@oslomet.no', 's349030@oslomet.no', 's356478@oslomet.no', 's341357@oslomet.no', 's351663@oslomet.no', 's309731@oslomet.no', 's339955@oslomet.no', 's319483@oslomet.no', 's333704@oslomet.no', 's329925@oslomet.no', 's339974@oslomet.no', 's306631@oslomet.no', 's351662@oslomet.no', 's351643@oslomet.no', 's148181@oslomet.no', 's306386@oslomet.no', 's193352@oslomet.no', 's350144@oslomet.no', 's324031@oslomet.no', 's326311@oslomet.no', 's325964@oslomet.no', 's331042@oslomet.no', 's305345@oslomet.no', 's326287@oslomet.no', 's351661@oslomet.no', 's350284@oslomet.no', 's315695@oslomet.no', 's351655@oslomet.no', 's237418@oslomet.no', 's180063@oslomet.no', 's351644@oslomet.no', 's345523@oslomet.no', 's349363@oslomet.no', 'anisy@oslomet.no', 's355988@oslomet.no', 's351657@oslomet.no'] 
allemails = ['s351656@oslomet.no', 's356528@oslomet.no', 's350141@oslomet.no', 's326326@oslomet.no', 's341354@oslomet.no', 's341358@oslomet.no', 's309854@oslomet.no', 's341474@oslomet.no', 's349771@oslomet.no', 's326609@oslomet.no', 's326151@oslomet.no', 's348572@oslomet.no', 's236646@oslomet.no', 's188110@oslomet.no', 's329926@oslomet.no', 's171212@oslomet.no', 's325909@oslomet.no', 's319478@oslomet.no', 's341460@oslomet.no', 's166126@oslomet.no', 's339971@oslomet.no', 's356469@oslomet.no', 's325920@oslomet.no', 's198759@oslomet.no', 'laszloer@oslomet.no', 's346664@oslomet.no', 's182417@oslomet.no', 's310338@oslomet.no', 's235401@oslomet.no', 's321045@oslomet.no', 's350110@oslomet.no', 's173307@oslomet.no', 's348002@oslomet.no', 's356066@oslomet.no', 's348588@oslomet.no', 'tomglove@oslomet.no', 's319482@oslomet.no', 's234031@oslomet.no', 's349473@oslomet.no', 's341467@oslomet.no', 's315740@oslomet.no', 'solvorho@oslomet.no', 's349009@oslomet.no', 's356550@oslomet.no', 's351659@oslomet.no', 's340018@oslomet.no', 's351646@oslomet.no', 's331043@oslomet.no', 's310455@oslomet.no', 's314769@oslomet.no', 's336602@oslomet.no', 's351645@oslomet.no', 's319470@oslomet.no', 's319496@oslomet.no', 's345532@oslomet.no', 's108343@oslomet.no', 's315310@oslomet.no', 's169909@oslomet.no', 's326178@oslomet.no', 's325936@oslomet.no', 's150048@oslomet.no', 's351653@oslomet.no', 's309855@oslomet.no', 's326166@oslomet.no', 's351654@oslomet.no', 's349030@oslomet.no', 's356478@oslomet.no', 's341357@oslomet.no', 's351663@oslomet.no', 's309731@oslomet.no', 's339955@oslomet.no', 's319483@oslomet.no', 's333704@oslomet.no', 's329925@oslomet.no', 's339974@oslomet.no', 's306631@oslomet.no', 's351662@oslomet.no', 's351643@oslomet.no', 's148181@oslomet.no', 's306386@oslomet.no', 's193352@oslomet.no', 's350144@oslomet.no', 's324031@oslomet.no', 's326311@oslomet.no', 's325964@oslomet.no', 's331042@oslomet.no', 's305345@oslomet.no', 's326287@oslomet.no', 's351661@oslomet.no', 's350284@oslomet.no', 's315695@oslomet.no', 's351655@oslomet.no', 's237418@oslomet.no', 's180063@oslomet.no', 's351644@oslomet.no', 's345523@oslomet.no', 's349363@oslomet.no', 'anisy@oslomet.no', 's355988@oslomet.no', 's351657@oslomet.no'] 
lastActivity = ['13 Sep at 19:49', '13 Sep at 22:25', '9 Sep at 23:39', '6 Sep at 20:06', '14 Sep at 9:31', '25 Aug at 10:11', '13 Sep at 17:16', '5 Sep at 17:22', '12 Sep at 17:53', '14 Sep at 9:29', '9 Sep at 13:42', '12 Sep at 23:16', '11 Sep at 16:40', '9 Sep at 13:24', '10 Sep at 13:38', '9 Sep at 17:23', '9 Sep at 18:10', '10 Sep at 10:41', '8 Sep at 11:39', '13 Sep at 14:40', '14 Sep at 9:05', '13 Sep at 14:11', '28 Aug at 1:11', '14 Sep at 10:07', '30 Aug at 12:02', '14 Sep at 9:25', '11 Sep at 9:30', '12 Sep at 12:47', '13 Sep at 22:57', '14 Sep at 8:20', '14 Sep at 8:30', '13 Sep at 16:37', '13 Sep at 23:13', '11 Sep at 16:47', '12 Sep at 0:12', '14 Sep at 8:33', '14 Sep at 9:16', '9 Sep at 10:28', '9 Sep at 14:22', '13 Sep at 17:08', '12 Aug at 10:47', '14 Sep at 0:10', '9 Sep at 11:21', '9 Sep at 18:18', '14 Sep at 8:08', '14 Sep at 10:05', '11 Sep at 15:07', '10 Sep at 8:54', '13 Sep at 17:32', '21 Aug at 12:04', '9 Sep at 15:55', '19 Aug at 11:52', '10 Sep at 0:04', '12 Sep at 0:12', '27 Aug at 15:11', '10 Sep at 0:29', '19 Aug at 13:12', '10 Sep at 8:13', '10 Sep at 22:01', '13 Sep at 17:43', '10 Sep at 21:15', '13 Sep at 17:54', '14 Sep at 10:00', '13 Sep at 13:03', '2 Sep at 23:36', '11 Sep at 11:12', '14 Sep at 3:24', '13 Sep at 20:29', '12 Sep at 15:01', '9 Sep at 11:45', '10 Sep at 9:57', '14 Sep at 8:47', '12 Sep at 21:33', '19 Aug at 14:23', '13 Sep at 18:38', '11 Sep at 11:12', '9 Sep at 11:40', '13 Sep at 14:18', '9 Sep at 9:57', '9 Sep at 18:40', '12 Sep at 23:51', '11 Sep at 0:07', '9 Sep at 12:24', '14 Sep at 9:35', '13 Sep at 23:50', '13 Sep at 20:11', '14 Sep at 0:32', '11 Sep at 13:11', '11 Sep at 13:11', '14 Sep at 9:00', '13 Sep at 23:06', '13 Sep at 18:05', '13 Sep at 19:20', '13 Aug at 12:46', '13 Sep at 21:59', '13 Sep at 16:57'] 
studentID = ['fs:215:1027378', 'fs:215:967714', 'fs:215:1028618', 'fs:215:842244', 'fs:215:895439', 'fs:215:948450', 'fs:215:781193', 'fs:215:885536', 'fs:215:856916', 'fs:215:876761', 'fs:215:842285', 'fs:215:514815', 'fs:215:671807', 'fs:215:523165', 'fs:215:880815', 'fs:215:374752', 'fs:215:854443', 'fs:215:851374', 'fs:215:940051', 'fs:215:566546', 'fs:215:938938', 'fs:215:566409', 'fs:215:841188', 'fs:215:576174', 'fs:215:994874', 'fs:215:801068', 'fs:215:478001', 'fs:215:820602', 'fs:215:659802', 'fs:215:773252', 'fs:215:1042316', 'fs:215:400857', 'fs:215:1012135', 'fs:215:966087', 'fs:215:1031718', 'fs:215:1000799', 'fs:215:836987', 'fs:215:654861', 'fs:215:842019', 'fs:215:947531', 'fs:215:714785', 'fs:215:107290', 'fs:215:1045598', 'fs:215:1068171', 'fs:215:996247', 'fs:215:943307', 'fs:215:1003814', 'fs:215:911736', 'fs:215:730685', 'fs:215:792905', 'fs:215:927864', 'fs:215:728310', 'fs:215:833283', 'fs:215:833562', 'fs:215:970370', 'fs:215:814316', 'fs:215:389641', 'fs:215:838008', 'fs:215:787808', 'fs:215:258328', 'fs:215:1045230', 'fs:215:783125', 'fs:215:862407', 'fs:215:1029529', 'fs:215:660102', 'fs:215:940801', 'fs:215:942722', 'fs:215:993850', 'fs:215:786909', 'fs:215:942125', 'fs:215:836235', 'fs:215:906775', 'fs:215:879428', 'fs:215:940949', 'fs:215:710796', 'fs:215:1038950', 'fs:215:657334', 'fs:215:256526', 'fs:215:674457', 'fs:215:524562', 'fs:215:1029574', 'fs:215:429476', 'fs:215:844909', 'fs:215:846932', 'fs:215:905337', 'fs:215:655483', 'fs:215:847106', 'fs:215:1045760', 'fs:215:1012859', 'fs:215:797646', 'fs:215:1037937', 'fs:215:627444', 'fs:215:422770', 'fs:215:1010700', 'fs:215:955355', 'fs:215:1044916', 'fs:215:624019', 'fs:215:1006040', 'fs:215:1032851'] 
totalhrs = ['03:23:55', '12:37:56', '10:22:15', '02:33:31', '15:51:31', '07:18', '02:07:12', '02:13', '09:52:46', '07:24', '09:08:32', '13:08:56', '07:11:52', '03:21:56', '03:26:53', '04:49:01', '11:52:55', '04:42:54', '01:27:18', '03:02:35', '13:06:09', '04:07:00', '58:53', '08:11:47', '01:12:59', '03:12:41', '39:24:19', '08:12:20', '10:29:01', '02:22:16', '12:03:51', '50:10:44', '35:39:54', '07:03:07', '39:32:00', '04:56:43', '32:51:56', '01:08:40', '02:42:58', '24:15:49', '06:16:09', '53:46', '03:20:33', '06:39:55', '19:04:03', '01:58:44', '07:31', '13:00:09', '05:16', '08:02:05', '03:21:43', '02:05:44', '09:01', '04:05:09', '12:07', '01:01:03', '02:46:31', '01:32:46', '16:00:07', '09:44:35', '05:25:42', '02:35:13', '27:27:45', '01:18:51', '21:14:30', '10:21:27', '37:32', '01:41:52', '06:27:05', '17:17:58', '44:24', '23:46:18', '09:05', '03:03:24', '03:47:15', '22:20:01', '08:00:35', '02:20:24', '59:31:59', '01:10:11', '15:06:37', '08:20:06', '05:36', '08:39:45', '07:33:17', '01:25:41', '41:38:02', '17:26:33', '09:28:22', '02:00', '09:11:00', '07:59:54'] 
nameList = ['Pernille Aaby', 'Sushil Acharya', 'IOANNIS ADAMOPOULOS', 'Cato Hilmi Akay', 'Alyaa Abdulkhaleq Abduljabbar Al-Jasim', 'Anantha Padmanaban Balasubramanian', 'Abdifatah Ali Bashi', 'Houda Benzazah', 'Andrey Bliznyuk', 'Kristian Brathovde', 'Bo Magnus Bratsberg', 'Cathrine Kieu Trang Bui', 'Arham Nadeem Butt', 'Karan Singh Chaudhary', 'Muhammad Ibraheem Cheema', 'Jasotharan Cyril', 'Nicklas Risan Dahl', 'Kassahun Gedlu Degena', 'Solomon Legesse Desalegn', 'Sujan Devkota', 'Marta Ewa Dubas', 'Patrick Ellefsen', 'Lars Iver Erdal-Aase', 'Laszlo Erdodi', 'John Inge Erlandsen', 'Jan Andre Fagereng', 'Felix Fritz', 'Vasavi Ganugapeta', 'Robel Michael Gebregergis', 'Mhd Tarek Mhd Roshdi Ghazal', 'Tom Glover', 'Anders Berg Gorboe', 'Odin Kanstad Grimstvedt', 'Shashank Gupta', 'Alexander William Ingvarsson Hals', 'Solvor Horrig Helland', 'Jon-Olav Holland', 'Marius Hornslien', 'Chaudhry Rehan Ikram', 'Asim Irshad', 'Muhammad Anwar Ul Haq Islam', 'Nazrul Islam', 'Christian Ruben Alexander Jahren', 'Hitesh Mohan Kaushik', 'Elias Khan', 'Rameen Jamshaid Khan', 'Magnus Kjelsaas', 'Boushra Kolko', 'Martin Kot', 'Josef Jan Krivan', 'Pawel Michal Kur', 'Piotr Jan Kusnierz', 'Denis Larsen', 'Monica Sofie Larsen', 'Thomas Leirvik', 'Ludvik Karlsson Lund', 'Mathias Hanstad Lundby', 'Assem Maratova', 'Nora Alexandra Cordasevschi Marcoux', 'Meraj Mostamand Kashi', 'Ahmed Mustafa', 'Rashmi Ganapati Naik', 'Irfanullah Nazand', 'Joyce Ndalaye', 'Rabin Parajuli', 'OMID PARSA MEHR', 'Fredrik Haugerud Pedersen', 'Darius Grigore Pop', 'Nourhan Ragab', 'Olav Hartvig Breivik Rui', 'Maria Safdar', 'Abdulkarim shlal', 'Linett Simonsen', 'Tine-Lovise Storvoll', 'Matrika Subedi', 'Samaneh Taghizadeh', 'Tahzeena Asif Tandel', 'Kaniz Fatema Tuly', 'Ramesh Upreti', 'Beebu Nisha Yasar Arafath', 'Syeda Ambreen Yawar', 'Shayan Yazdanmehr', 'Anis Yazidi', 'Nimra Zainab', 'Mahshidsadat Zolfaghariejlalmanesh'] 
nameList2 = ['Sushil Acharya', 'IOANNIS ADAMOPOULOS', 'Alyaa Abdulkhaleq Abduljabbar Al-Jasim', 'Bo Magnus Bratsberg', 'Nicklas Risan Dahl', 'Marta Ewa Dubas', 'Lars Iver Erdal-Aase', 'Felix Fritz', 'Vasavi Ganugapeta', 'Robel Michael Gebregergis', 'Mhd Tarek Mhd Roshdi Ghazal', 'Tom Glover', 'Alexander William Ingvarsson Hals', 'Marius Hornslien', 'Christian Ruben Alexander Jahren', 'Elias Khan', 'Thomas Leirvik', 'Nora Alexandra Cordasevschi Marcoux', 'Joyce Ndalaye', 'Rabin Parajuli', 'OMID PARSA MEHR', 'Nourhan Ragab', 'Olav Hartvig Breivik Rui', 'Samaneh Taghizadeh', 'Beebu Nisha Yasar Arafath', 'Syeda Ambreen Yawar'] 
nameAug = ['Anantha Padmanaban Balasubramanian', 'Lars Iver Erdal-Aase', 'John Inge Erlandsen', 'Solvor Horrig Helland', 'Rameen Jamshaid Khan', 'Boushra Kolko', 'Piotr Jan Kusnierz', 'Monica Sofie Larsen', 'Anis Yazidi'] 

oslometemail.sort()
question1.sort()
if oslometemail == question1: 
    print('question 1 done')
else:
    #listdiff = question1.sort() - oslometemail.sort()
    listdiff = [item for item in oslometemail if item not in question1]

    print('The difference =', listdiff)
    



