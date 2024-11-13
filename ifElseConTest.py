import math

area = float(input("Enter the area of your circle:  "))

if area > 0: 
    radius = math.sqrt(area/math.pi)
    print("The radius of your circle is: ",radius)
else: 
    print("Error: The area must be a positive number.")
    area = float(input("Enter the area of your circle:  "))


print("\n\n\n Part 2 of the application: \n\n\n")

first = int(input("Enter your first positive number: "))

second = int(input("Enter your second positive number: "))


# More code goes here 
if first > second: 
    highest = first
    lowest = second
else: 
    highest = second
    lowest = first
# Final state of the program 

print("The HIGHEST number is: ",highest)
print("The LOWEST number is: ",lowest)


print("\n\n\n Part 3 of the application: \n\n\n")
print("Logical Opperraters and Compound Boolean expressions")
print("-----------------------------------------------\n\n\n")

number = int(input("Enter students numeric grid: "))
# if number > 100: 
#     print("Error: Grade must be between 100 and 0.")
# elif number < 0:
if number >= 100 or number <= 0: ### Compound Conditional 
# If number < 0 or number > 100 
    print("Error: Grade must be between 100 and 0.")
else: 
    # Code to convert numeric grade to Letter Grade goes here
    # Create a function: letterGrade():
    # Coverts number to A, B, C, D, F
    # A >= 90, B >= 80, C >= 70, D >= 60, F < 60

    if number >= 90: 
        print("Your letter grade is an A.") 
    elif number >= 80 and number <= 89:
        print("Your letter grade is a B.")
    elif number >= 70 and number <= 79: 
        print("Your letter grade is a C.")
    elif number >= 60 and number <= 69: 
        print("Your letter grade is a D.")
    else: 
        print("Your letter grade is an F, for FAILURE.") 

