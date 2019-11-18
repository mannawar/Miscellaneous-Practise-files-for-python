# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 12:52:59 2019

@author: Mannawar Hussain
"""
from sys import argv
script, first, second, third = argv
print ("The script is called:", script)
print ("yoyr first variable is:", first)
print ("your third variable is:", third)

from sys import argv
script, user_name = argv
prompt = '>'
print (f"Hi (user_name), I'm the {script} script.")
print ("I'd like to ask you few questions.")
print (f"Do you like me {user_name}?")
likes = input (prompt)
print (f"Where do you live {user_name}?")
lives = input (prompt)
print ("What kind of computer do you have?")
computer = input (prompt)
print ("""Alright, so you said {likes} about liking me. you live in {lives}. Not sure where that is.
       And you have a {computer} computer.Nice""")

