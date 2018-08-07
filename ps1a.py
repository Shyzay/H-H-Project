# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:26:56 2018

@author: KELS
"""
#Time taken to get the savings for down payment initialized to 0
time_taken = 0

#Annual rate return
r = 0.04

#Current savings in the account
current_savings = 0

#Inputs taken
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#Portion saved from monthly salary
portion_saved = portion_saved * (annual_salary/12)

#Down payment to be made 
portion_down_payment = 0.25 * total_cost

while current_savings<= portion_down_payment:
    
    #Current savings to be increased monthly
    current_savings += (current_savings*r/12) + (portion_saved)
    
    #Time taken for increment
    time_taken = time_taken + 1


print("Number of months is: %d" %(time_taken))
    

