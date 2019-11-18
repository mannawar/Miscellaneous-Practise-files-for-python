# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:17:13 2019

@author: Mannawar Hussain
"""

x = float(input("Enter your annual salary:"))
y= float(input("Enter the percent of salary to save, as decimal input:"))
z= float(input("Enter the cost of your dream home: "))
semi_annual_raise= float(input("Enter semi annual raise of your salary, as a decimal input:"))


monthly_savings = (x/12)*(1+semi_annual_raise)*y 
semi_annual_raise+=6
portion_down_payment = 0.25
down_payment = portion_down_payment * z

annual_return =0.04
current_saving = 0.0
number_of_months = 0

while current_saving<down_payment:
    current_saving += monthly_savings + (current_saving * annual_return)/12 
    number_of_months += 1
       
print("Number of months: {}".format(number_of_months))
