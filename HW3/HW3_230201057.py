# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 22:25:58 2016

@author: fey
"""   
#230201057

def mainmenu():  
    print "   Main Menü:"
    print "1. List all contacts"
    print "2. Find contact"
    print "3. Add contact"
    print "4. Remove contact"
    print "5. Save and quit"
    option=raw_input("   Enter an option:")
    return option
    
def format_number(numbers):
    format_number=tuple(numbers) #for duplicate list numbers step1
    format_number=list(format_number) #for duplicate list numbers step2
    c=0 #help tracking index of format_number
    formatted_number=[] #intialize empty list
    for i in format_number:#sequentially takes phone number from format_number
        a=list(format_number[c])#convert phone number from string to a list example["1","2"]
        a.insert(3," ")#add space before index 3 example ["5","0","5"," ","1","2","3","4","5","6","7"]
        a.insert(7," ")#add space before index 7 important after first insert index number is changed 
        c=c+1#help tracking index of format_number
        b=""#intialize empty string for concatenate list a's elements
        for i in a:#concatenating process
            b=b+i
        formatted_number.append(b)#when finished concatenating add element in formatted_number
    return formatted_number#return formatted version in formatted_number DDD DDD DDDD
    
def query_name(name,names):#expected names is a sequence
    for i in names:#it goes in the names' elements and look for matching
        if i.lower()==name.lower():#controling matched element
            index_name=names.index(i)#take index of matched element
            return index_name  
            
def valid_number(new_number):
    try:
        int(new_number)
        counter=0
    except ValueError:
        print("This phone number is invalid.")
        counter=1 #signal: if it isn't a sequences of number we don't need control its lengths
        return False #help us to know circumtance of validity
    if len(new_number)!=10 and counter!=1:
        print "This phone number is invalid."
        return False  #help us to know circumtance of validity
#####Start initializing and format data######
print "\n>>>Example directory for linux /home/fey/Desktop/contacts.txt"
print ">>>Example directory for Windows C:/Users/furka/Desktop/contacts.txt"    
path=raw_input("Please type contacts.txt path:")
contacts=open(path,'r')
read_contacts=contacts.readlines()
names=[] #create empty sequence for names
numbers=[]#create empty sequence for numbers
#I prefer to use paralel list so names and numbers is paralel list
if read_contacts!=[]:#empty file control
    a=0 #counter help tracking index of list
    for i in read_contacts:
        c_split=str.split(read_contacts[a],"#")
        names.append(c_split[0])
        numbers.append(c_split[1])
        a=a+1 #counter help tracking index of list
    last_char=numbers[-1]
    if last_char[-1]!="\n":#control last char of last element
       numbers[-1]=numbers[-1]+"\n"
#####End of initilizaling and format data####

while True:#for continuity of the program
    option=mainmenu()
    b=0 #counter help tracking index of list
    if option=="1":#list all contacts operation
        for i in names:
            print i,format_number(numbers)[b] #names and formatted number are printed
            b=b+1 #counter help tracking index of list
    elif option=="2":#find contact operation
        name=raw_input("Please type a name to find:")
        query_result=query_name(name,names) #make an query in the data,if it found any match return index of this element
        if type(query_result)==int:#if type equal int we understand it return index of matched element
            print format_number(numbers)[query_result] #print matched phone number
            option2=raw_input("1.Edit Name, 2.Edit Phone Number, 3.Continue\n")
            if option2=="1":#edit name operation
                new_name=raw_input("Enter a new name:")
                query_result2=query_name(new_name,names)#same logic
                if type(query_result2)==int:#same logic
                  print "This person already exist"
                else:
                    names[query_result]=new_name #if no matched name, it changes name into new_name
                    print "Contac list updtated"
            elif option2=="2":#edit phone number
                new_number=raw_input("Enter a new number:")
                valid_result=valid_number(new_number)#if valid_number return false it means no valid input
                if valid_result!=False:#otherwise number is valid
                    numbers[query_result]=new_number+"\n" #it changes numer into new_numer+"\n"(it related structure of program)
                    print "Contac list updated"
        else:
            print "No such contac exist."
        
    elif option=="3":#add contact operation
        new_name=raw_input("Enter a new name:")
        query_result3=query_name(new_name,names) #same logic
        if type(query_result3)==int:#same logic
            print "This person already exist."
        else: 
            new_number=raw_input("Enter a number:")
            valid_result2=valid_number(new_number)#same logic
            if valid_result2!=False:#same logic
                names.append(new_name)#it adds new_name into names list
                numbers.append(new_number+"\n")#it adds new_number into numbers list
                print "New contact is added."
    elif option=="4":#remove contact operation
        name=raw_input("Enter a name:")
        query_result4=query_name(name,names)#same logic
        if type(query_result4)==int:#same logic
            names.pop(query_result4)#it remove element in names which has query_result4 index
            numbers.pop(query_result4)#it remove element in numbers which has query_result4 index
            print "Contact is removed."
        else:
            print "No such contact exist."   
    elif option=="5":#save and quit operation
        contacts.close()#it close contacts.txt file
        contacts=open(path,'w')#it open file with permission of writing
        c=0 #counter for tracking indexs
        for i in names:#start concatenating operation before writing data into file
            contacts.write(names[c]+"#"+numbers[c])#it arranges line for writing and write line by line into file
            c=c+1 #counter for tracking indexs
        contacts.close() #close contacts.txt file for finishing writing operation
        break #kill the program
    else:
        print "Invalid option entered"

#fey


