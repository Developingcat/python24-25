"""
This program asks the user for their name and age, 
and it handles the case where the user fails to enter a valid integer for their age.
"""



name = input("Please enter your first name: ")
age = -1 

try: 
    age = int(input("Please enter your age: "))
except ValueError:
    print("That wasn't a number, you DUMBDUMB.")


# Print name and age, using the default age is user did not enter in an integer 

print("Name: " + name)

if age == -1 :
    try: 
        age = int(input("Please re-enter your age: "))
    except ValueError:
        print("I literally gave you two chances, and you failed them both.")
        age = "You sadden me, fool."

print("Age: " + str(age))



