# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:38:28 2019

@author: Mannawar Hussain
"""
hi = "Hello there"
name = "Mannawar"
greet = hi+name
print (greet)
greeting = hi+ " " +name
print (greeting)
silly = hi + (" "+ name)*3
print (silly)
x = 1
print (x)
x_str = str(x)
print ("my fav num is", x, ".", "x=", x)
print ("my fav num is", x_str + "." + "x=" + x_str)
print ("my fav num is" + x_str + "." + "x=" + x_str)

text = input ("Type anything...")
print (5*text)
num = int(input ("Type anything..."))
print (5*num)

# program legends of zelda-lost woods
n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
     n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
print("\nYou got out of the Lost Forest!\n\o/")



mysum = 0
for i in range (7, 10):
    mysum += i
print(mysum) 




