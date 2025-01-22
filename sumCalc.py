"""
Name: Hannah O'Shea 
Date : 1/22/2025
File: sumCalc.py
"""




# Asking for the numbers from the user 

numberOne = int(input("Please enter in a number: "))

numberTwo = int(input("Please enter in another number: "))

numberThree = int(input("Please input a third number: "))

numberFour = int(input("Please enter in a fourth, cool, number: ")) 

numberFive = int(input("Please enter in a fifth, even cooler, number: "))

# Defining the sums, because oh boy this is going to be a LOT 




# Adds the numbers -> Possibly put a try and except here to make sure that the input is actually a number and not
# some odd number thingy. Maybe use a if/else statement in here? 

# How it'll add the numbers; possible adds two together at a time, and then the result with the fifth number? 
# This will absolutely need a try and except, remember that. 

def number_addition(): 
    resultOne = numberOne + numberTwo 
    resultTwo = numberThree + numberFour 
    resultOfTwo = resultOne + resultTwo 
    resultSix = resultOfTwo + numberFive 
    print(resultSix)

number_addition()
    






# Prints the output