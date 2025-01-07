"""
This program will accept 2 inputs from the user and process the data as exponets of one another 
"""

# This function prints the 2 user inputs and then calculates them as exponents of one another and prints them out to the terminal window. 

def myFunction(a, b):
    print("\n Variable A is: ", a, ".")
    print("\n Variable B is: ", b, ".")
    exp1 = a ** b
    exp2 = b ** a
    print("\n", a, "to the power of",b , "is: ", exp1)
    print("\n", b, "to the power of",a , "is: ", exp2)



def sum(first, second): 
    total = first + second 
    print("The total of your data input is" ,total)




# Ask the user for 2 integers between 1 and 10
a = int(input("\nPlease enter a number between 1 and 10: "))

b = int(input("\nPlease enter a number between 1 and 10: "))


myFunction(a, b)


print ("\nPart 2 of our Example:")

# Give the user the option to repeat this process as many times as they want, if a quit is warrented, they type the word Quit. 
# Have users input positive integers 



while True:
    myVar1 = int(input("Please enter a positive whole number: "))
    myVar2 = int(input("Please enter a positive whole number: "))
    sum(myVar1, myVar2)
    number = input("Would you like to repeat this process? Enter yes if so, enter no if no: ")
    
    if number == 'no':
        break 
    else: 
        print("Back to the top.")



# Call the sum function to process the user input 





