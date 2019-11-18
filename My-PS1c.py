# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:01:51 2019

@author: Mannawar Hussain
"""

user_salary = float(input("Enter the starting annual Salary : "))
semi_annual_raise = .07
Annual_return = 0.04
portion_of_down_payment = 0.25
cost_of_the_house = 1000000
down_payment= cost_of_the_house * portion_of_down_payment

one_hundred_dollar_as_epsilon = 100
steps_in_bisection_search = 0
possible_to_pay_in_3_years = True
max_portion_saved_as_an_integer = 10000
min_portion_saved_as_an_integer = 0
best_portion_saved_as_an_integer = max_portion_saved_as_an_integer 


while True:
    steps_in_bisection_search +=1
    annual_salary = user_salary
    best_portion_saved = best_portion_saved_as_an_integer/10000
    monthly_savings = (annual_salary/12) * best_portion_saved
    
    current_savings = 0
    number_of_months = 0
    while number_of_months <=36:
        current_savings += monthly_savings + ((current_savings*Annual_return)/12)
        number_of_months +=1
        if  number_of_months % 6 ==0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary/12) * best_portion_saved

    if abs(current_savings-down_payment) <= one_hundred_dollar_as_epsilon:
        break
    if current_savings> down_payment:
        max_portion_saved_as_an_integer = best_portion_saved_as_an_integer
        
    else:
        min_portion_saved_as_an_integer = best_portion_saved_as_an_integer
        
    if min_portion_saved_as_an_integer >= max_portion_saved_as_an_integer:
        possible_to_pay_in_3_years = False
        break
    best_portion_saved_as_an_integer = (max_portion_saved_as_an_integer + min_portion_saved_as_an_integer)//2
    
if possible_to_pay_in_3_years:
    print("Best saving rate: {}" .format(best_portion_saved))
    print ("Steps in bisection search:{}" .format(steps_in_bisection_search))
else:
    print("It is not possible to pay the down payment in three years.")        




# Another way to calculate best rate of savings
    
annual_salary = float(input('Enter your starting salary: '))
x = annual_salary
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25 * total_cost
months = 0
epsilon = 100
low = 0
high = 10000
step = 0   


while True:
    portion_saved = (low+high)/2
    annual_salary = x
    current_savings = 0
    for mo in range (0, 36):
        monthly_salary = annual_salary/12
        current_savings = current_savings + ((monthly_salary*portion_saved)/10000)+(current_savings * 0.04)/12
        if mo%6 == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
    if abs(current_savings - portion_down_payment) <= epsilon:
        print ("Best Saving rate:", '%.2f' %(portion_saved/100), '%')
        print('step in binary search:', step)
        print (current_savings)
        break
    elif (current_savings-portion_down_payment) > epsilon and current_savings >portion_down_payment:
        high = portion_saved
        
    elif(current_savings - portion_down_payment) > epsilon and current_savings < portion_saved:
        low = portion_saved
    if low == high:
        print("It is not possible to pay down payment in 3 years.")
        break
    step=step+1
        
        
        
        




























































# =============================================================================
# down_payment_to_be_made_in_36_months = 250000
# 
# saving_required_per_month = 6944
# 
# required_rate_of_saving_monthly = (saving_required_per_month//user_salary)
# 
# if saving_required_per_month < 100:
#     print("Its not possible to save for the down payment for the mentioned salary")
#     
# else:
#     print ("Rquired rate of monthly saving is :{} ", required_rate_of_saving_monthly)
#     
# =============================================================================
