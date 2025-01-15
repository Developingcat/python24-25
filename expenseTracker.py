"""
Title : expenseTracker.py with Category Summaries 
Author : Hannah O'Shea 

Description: 
This program allows users to add expenses with categories, view the total expenses, and see a summary of expenses by category. 
It uses functions with multiple steps, internal calculations, and return values. 

Choose an option 

Application Menu: 
    1. Add expense 
    2. View total expenses 
    3. View expense report - Broken down into two functions ( 1. Get summary , 2. display summary)
    4. Quit 


Four primary processes based on the options on the menu 

Processes(Functions):
    1. Add expense 
    2. View total 
    3. View report 

Data Structure: 
    myDictonary{
       key1: value1 
       key2: value2 
       .... 
       keyn: valuen
   }
"""

# Define the functions for an application 

def add_expenses():
    add = 1 + 1 # Remove later

def get_total_expenses():
    add = 1 + 1 # Remove later

def get_category_summary():
    add = 1 + 1 # Remove later

def display_expense_report():
    add = 1 + 1 # Remove later

while True: 
    print("\n\n")
    print("###############################")
    print("\n")
    print("##### MY EXPENSE TRACKER. #####")
    print("\n")
    print("###############################")
    print("\n\n")
    


    # Created the application menu, 
    print("######################")
    print("####### MENU #########")
    print("######################")
    print("\n\n")
    print("\n1. Add Expense.")
    print("###################")
    print("\n2. View Total Expense.")
    print("###################")
    print("\n3. View Expense Report.")
    print("###################")
    print("\n4. Quit")

    # Ask the user what they want to do 
    choice = input("Enter your choice: ")

    # End the application and avoid an infinite loop 
    if choice == "4":
        break 






