# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:50:32 2018

@author: KELS
"""

#Time taken to get savings to down payment initialized to 0
time_taken = 0

#Annual return rate
r = 0.04

#Current saving in account
current_savings = 0

#Take user input
annual_salary = float(input("Enter your annual salary: "))
portion_saved_percent = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

#Monthly salary
monthly_salary = annual_salary/12

#Portion saved from monthly salary
portion_saved = portion_saved_percent * monthly_salary

#Down payment to be made
portion_down_payment = 0.25 * total_cost
 
while current_savings <= portion_down_payment:
    
    #Current savings to be increased monthly
    current_savings += (current_savings * r/12) + portion_saved    
    
    
    
    #Increment time_taken
    time_taken += 1
    
    if time_taken % 6 == 0:
        
        monthly_salary = (semi_annual_raise * monthly_salary) + monthly_salary 
        
        portion_saved = portion_saved_percent * monthly_salary
    
   

print("Number of months is: %d" %(time_taken))