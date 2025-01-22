"""
This program tries to retrieve an integer from the user. If the user enters something other then an integer; 
the program handles it by printing an error.
"""
try:
    my_number = int(input("Please enter an integer: "))
    print("Your number: " + str(my_number))
except ValueError:
    print("That wasn't a integer, you FOOL.")

print("See...the program is still running.")