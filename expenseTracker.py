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

def add_expenses(expenses, category, amount):
    # Add an expense to the tracker, our arguements, expanses (dict): A dictionary where keys are categories and values are list
    # Category string, the category of expense 
    # Amount (Float), the amount of the expense 
    # Returns: The update dictionary of expenses 
    if category not in expenses: 
        expenses[category] = [] 
    expenses[category].append(amount)
    
    return expenses

def get_total_expenses(expenses):
    #Calculate the total expenses across all categories 
    #Args (dict) : A dictionary where keys are categories and values are list expense amount 
    # Return : Float, the total amount of expenses 
    return sum(sum(amounts) for amounts in expenses.values())

def get_category_summary(expenses):
    # Provide a summary of expenses by category 
    # Argument: expenses (dict) A dictionary where keys are categories and values are lists of expense amounts 
    # Return : Dict, our ever expanding dictionary 
    return {category: sum(amounts) for category, amounts in expenses.items()} 


def display_expense_report(expenses):
    # Display a detailed expense report 
    # Argument: Expenses (dict) A dictionary where keys are categories and values are lists of expense amounts 
    # Returns : None 
    print("\n--- Expense Report ---")
    category_summary = get_category_summary(expenses)
    total_expenses  = get_total_expenses(expenses)

    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")

    print(f"Total Expenses: ${total_expenses:.2f}")
    print("-------------------------------------")

# Create an empty dictionary to hold all of our data

expenses = {}
    
print("\n")
print("###############################")
print("\n")
print("##### MY EXPENSE TRACKER. #####")
print("\n")
print("###############################")
print("\n\n")


while True: 
    
    


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
    # User has 4 options thus section will control what happens 
    if choice == "1":
        category = input("Enter the expense category (e.g. Food, Transportation, Utilities, etc.)")
        amount = float(input("Enter the expense amount: "))
        expenses = add_expenses(expenses, category, amount)
        # Expenses get turned from the function, and assigned to a functions variable
        print("Expense added successfully.")

    elif choice == "2": 
        total = get_total_expenses(expenses)
        print(f"Total expenses so far: ${total:.2f}")
    elif choice == "3": 
        display_expense_report(expenses)
    # End the application and avoid an infinite loop 
    elif choice == "4":
        break 
    else:
        print("Invalid choice, please choose again.")



