"""
Name: Hannah O'Shea 
Date : 1/22/2025
File: sumCalc.py
"""

try: 

# Asking for the numbers from the user 
 
    numberOne = int(input("Please enter in a number: "))

    numberTwo = int(input("Please enter in another number: "))

    numberThree = int(input("Please input a third number: "))

    numberFour = int(input("Please enter in a fourth, cool, number: ")) 

    numberFive = int(input("Please enter in a fifth, even cooler, number: "))

    numberSummary = numberOne + numberTwo + numberThree + numberFour + numberFive 


    print("Your number is", numberSummary)



except ValueError: 
    print("A number you inputed was incorrect or invalid, please try again.") 

# Defining the sums, because oh boy this is going to be a LOT 

# Try and except statements go here, me thinks 

# if numberOne == -1: 
#     try:
#         numberOne = int(input("Please re-enter the number you wish to put in: "))
#     except ValueError:
#         print("That wasn't a number.")


# Adds the numbers -> Possibly put a try and except here to make sure that the input is actually a number and not
# some odd number thingy. Maybe use a if/else statement in here? 

# How it'll add the numbers; possible adds two together at a time, and then the result with the fifth number? 
# This will absolutely need a try and except, remember that. 


# def number_addition(): 
#     resultOne = numberOne + numberTwo 
#     resultTwo = numberThree + numberFour 
#     resultOfTwo = resultOne + resultTwo 
#     resultSix = resultOfTwo + numberFive 
#     print(resultSix)

# number_addition()
