print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 1               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a number is positive, negative, or zero
number = -3

if number >= 0: 
    print("Your number is a positive.")
elif number > 0: 
    print("Your number is higher then zero, and a positive!")
else: 
    print("Your number is a negative......")



# Write an if/else (elif) structure to determine the number's positive, negative, zero state

print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 2               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a user has admin privileges
user_role = "admin"
userBase = user_role
userBaseQuestion = input("Please state your role within the computer system:  ")


# Write your Code Below

if userBaseQuestion == userBase: 
    print("You have admin! Merry Christmas!")
else: 
    print("You do not have admin privileges... leave.")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 3               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to check if a year is a leap year
# year = 2024
year = int(input("Enter in a year to check if it's a leap year:  "))
# Write your Code Below

if year % 4 == 0 and year % 100 != 0: 
    print("It's a leap year!") 
else: 
    year % 400 == 0 
    print("D'Awh, it's not a leap year...")


print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 4               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to classify age into age groups
age = 25
ageQuestion = int(input("How old are you?: "))
# Write your Code Below

if ageQuestion == age or ageQuestion >= 16: 
    print("Congrats! You are a young adult!")
elif ageQuestion == 16: 
    print("You're a teen!")
elif ageQuestion != 16: 
    print("You are not a teen!")



print("\n\n\n")
print("###########################################")
print("##                                       ##")
print("##              Practice 5               ##")
print("##                                       ##")
print("###########################################")
print("\n\n\n")

# Program to determine discount based on purchase amount
purchase_amount = float(input("How much would you like to spend today?: "))

# Write your code Below
DISC = float(00.20) 
amtDisc = float(purchase_amount * 00.20)
discountPrice = purchase_amount - amtDisc


print(float(discountPrice) , "was saved on.")
