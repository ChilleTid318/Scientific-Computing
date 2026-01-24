# -*- coding: utf-8 -*-
"""
Created on Fri Jan 23 19:30:18 2026

@author: aidan
"""
import time as ti #or 'import time as *'
from time import sleep #ti.sleep() delays the execution
import random as ra #or 'import random as *'
from random import randint #ra.randint(,) generates a random integer N such that a<=N<=b.
from random import choice #this chooses a random string in a sequence/list

debug_mode = True 

replies = ["It is certain", "Yes", "Most likely", "Very doubtful", "My reply is no", "no"] 

question = input("What is your question?") #if right, it should allow to input a question with a reply. YES IT DOES

print("Your question was:")
if debug_mode:
    ti.sleep(1)
print(question) #this should print 

#so do I have to use ra.randint? I'm having trouble with integers and implementing strings as a reply
"""replies_answer = ra.randint(0, replies+1)""" #doesn't work. How do this??!?!?
#In the random module: https://docs.python.org/3/library/random.html , there is random.choice() that can use strings

replies_answer = ra.choice(replies) #hopefully works.

print("My answer is:")
if debug_mode:
    ti.sleep(2)
#print(replies_answer) doesnt work
print(replies_answer)

#lets go it worked.




