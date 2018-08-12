# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:16:08 2016

@author: fey
"""
#230201057
print ">>>Example directory for linux /home/fey/Desktop/employee.txt"
print ">>>Example directory for Windows C:/Users/furka/Desktop/employee.txt"
my_file=raw_input("Please type directory of employee.txt:")
while True:
    signal=0
    name=raw_input("Please type an employee name:")
    open_file=open(my_file,'r')#for continuity of the program, new born,opens file
    line=open_file.readline()#reads first line
    if name.lower()=="quit":break #immediaty quit the program when typed value,case insensitve
    while(line!=""): #checks empty line
        counter=0  #catches magnitude of salary(2) and sale(3)
        for i in str.split(line," "): #finds space in the line
            counter=counter+1  
            if counter==2:
                salary=i
            if counter==3:
                sale=i
            if i.lower()==name.lower(): #catches valid name, case insensitive
                signal=signal+1 #gives information about this statement circumtance
        if signal==1: #it means, we found valid name
            signal=signal+1 #gives information about this statement circumtance
            print "Your name:",name.upper() #name become capital letters
            if 0<=int(sale)<5:
                print "Your Salary:",int(salary)
            elif 5<=int(sale)<10:
                print "Your Salary:",int(salary)+15
            elif 10<=int(sale)<25:
                print "Your Salary:",int(salary)+25
            elif int(sale)>=25:
                print "Your Salary:",int(salary)+50
        line=open_file.readline() #skip another line
    if signal!=2: #it means we didn't run line27(if signal==1)
        print "You didn't type a valid name please try again."
#fey
