# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:57:23 2016

@author: fey
"""
#230201057
def file_reader(source):#it reads file and convert content of file to a dictionary structure
    dictionary=(open(source,'r')).readlines()
    return dict([i.split("\t") for i in dictionary])
def binary_search(element,eng_tr):#basic binary search algorithm
    keys=eng_tr.keys()#take dictionary's keys
    keys.sort()
    low=0
    high=len(keys)-1
    while low<=high:
        mid=(low+high)/2
        item=keys[mid]
        if element==item:
            return keys[mid]
        elif element<item:
            high=mid-1
        else:
            low=mid+1
    return -1
def alternative_word(element,eng_tr):#eng_tr is in dictionary structure
    keys=eng_tr.keys()#take dictionay's keys
    flag=0#for information about statement
    for i in keys:
        if abs(len(i)-len(element))<6:#find absolute value of length diffrence
            if element in i and element!="":#substring and superstring control
                asking=raw_input("Did you mean(y/n):"+i+"?\n")
                if asking=="y":
                     return i #return english key
                     flag=1
                     break
                elif asking=="n":
                    return -2 
    if flag!=1:#we understand we can't find alternative word
        return -1
def length_difference(element,eng_tr):
    keys=eng_tr.keys()
    len_dif=[]
    for i in keys:
        dif=abs(len(element)-len(i))
        if dif==0:
            len_dif.append((i,0.5))
        else:
            len_dif.append((i,dif))
    return len_dif #(key,length_diffrence) is a list contain tuple in it
def letter_difference(element,eng_tr):#eng_tr is in dictionary structure
    keys=eng_tr.keys()#take dictionary's keys
    let_dif=[]
    for key in keys:
        temp=[]
        key_char=list(key)
        for char_element in element:
            if char_element in key_char:
                key_char.pop(key_char.index(char_element))#it deletes matching char in the list key_char
            else:
                temp.append(char_element)#if no matchin it adds this element temporary list
        temp=temp+key_char #concatenate list temp nad key_char(after removing matching char)
        let_dif.append((key,len(temp)))#let_dif is a list it contains tuple elements.
    return let_dif #it returns a list in format (key,letter_difference)
def distance(element,eng_tr):#eng_tr is in dictionary structure
    keys=eng_tr.keys()#take dictionary's keys
    a=zip(keys,range(len(keys)))#to help iteration create a list in format (key0,0),(key1,1)...
    pre_co=[[letter_difference(element,eng_tr)[i][1]*length_difference(element,eng_tr)[i][1],j] for j,i in a]
    """Explanation for pre_co:it creates a list with multiplication of letter diffrence and length difference"""
    d=0#to help indexing through list
    for j,i in pre_co:#pre_co is in format (let_dif*len_dif,key)
        if i[-1]==element[-1]:#control last char and multiply with coefficent value
            pre_co[d][0]=pre_co[d][0]*0.5
        if i[0]==element[0]:#control first char and multiply with coefficent value
            pre_co[d][0]=pre_co[d][0]*0.5
        #above I used to if stament not if elif structure because of I want to control each case independently
        d=d+1#increment d for future indexing
    pre_dict=dict(pre_co)#convert pre_co and it creates a dictionary consist of unique keys.
    key=min(pre_dict.keys())#(let_dif*len_dif*coefficent,...,...,..) find mimimum value for let_dif*len_dif*coefficent
    asking=raw_input("Did you mean(y/n):"+pre_dict[key]+"?\n") #to take information from user
    if asking=="y":#if it is valid
        return pre_dict[key]#return english key
    else:
        return -1
        
        
print "\n>>>Example directory for linux /home/fey/Desktop/dictionary.txt"
print ">>>Example directory for Windows C:/Users/furka/Desktop/dictionary.txt"   
eng_tr=file_reader(raw_input("\nPlease type a directory for dictionary.txt:"))
while True:#for repeating asking again and again    
    element=raw_input("Type word you want to search\nType x to quit\n")
    if element=="":#it does not allow empty string.
        element==""#it hasn't have any meaning just a formality
    elif element=="x":#if it is valid instantly terminate the program
        break
    else:
        search_result=binary_search(element,eng_tr)
        if search_result==-1:#search_result=-1 we undestand we cant find exact matching for element
           alternative_result=alternative_word(element,eng_tr)
           if alternative_result!=-1 and alternative_result!=-2:#it means we find a alternative matching
              print alternative_result+":"+eng_tr[alternative_result]
           elif alternative_result==-1 and alternative_result!=-2:#it means user don't say "n", we can't find alternative matching
              result_distance=distance(element,eng_tr)#we try to find the clotest word
              if result_distance!=-1:#it means we find a valid the clotest word.
                  print result_distance+":"+eng_tr[result_distance]
        else:
            print search_result+":"+eng_tr[search_result]#if we find any valid matching in binary search we display it.

#fey
    

