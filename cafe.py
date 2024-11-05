# Author : Hannah O'Shea 
# File : cafe.py
# Date : 11/5/2024

# Project: Café Bill Calculator:

# Description
# In this project, students will create a simple application that calculates the total bill for a café order. The program will prompt the user to enter the prices of various items ordered (coffee, pastry, and juice) and calculate the total. A service tax will also be added as a constant.
# Objectives
# Use print() to display messages to the user.
# Use input() to collect user input.
# Define and use variables and constants.
# Define a basic function to calculate the total bill.
# InstructionsDefine Constants:
# Define a constant for the service tax rate. The service tax should be set to 10%.

# Prompt User Input:
# Use input() to get the prices of each item from the user:
# Ask the user for the price of coffee.
# Ask the user for the price of pastry.
# Ask the user for the price of juice.
# Convert Input to Float:
# Convert each input to a float so calculations can be performed.

# Define a Function:
# Define a function calculate_total that:
# Takes three arguments for the prices of coffee, pastry, and juice.
# Adds these prices together.
# Calculates and adds the service tax to the total.
# Returns the final total.
# Display the Bill:Print the calculated total using print().

# Placing the constants! 

SERVICE_TAX = float(00.1) 

coffee = float(input("How much does a cup of coffee cost?: "))

pastry = float(input("How much does a pastry cost?: "))

juice = float(input("How much does a cup of juice cost?: "))


TOTAL_COST = coffee + pastry + juice 

WITH_TAX = TOTAL_COST * 00.1 

print("the total cost would be," ,TOTAL_COST, "and with tax, it'll be" ,WITH_TAX,)