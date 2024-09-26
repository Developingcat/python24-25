import math

area = float(input("Enter the area: "))

if area > 0:
    radius = math.sqrt(area / math.pi) 
    print("The Radius is", radius)
else:
    print("Error! The area MUST be a positive number!")
    area = float(input("Enter the area:"))
    radius = math.sqrt(area / math.pi)
    print("The radius is", radius)

print("\n\nExample 2: Maximum and Minimum Number")
print("---------------")

first = int(input("Enter the first number: "))
second = int(input("Enter second number here:"))

if first > second: 
    maximum = first 
    minimum = second 
else:
    maximum = second
    minimum = first 

print("Maximum number is: ", maximum)
print("Minimum number is: ", minimum)