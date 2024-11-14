print("Example 1:\n\n ")


# Program will check if number is even or odd 
# number = 7

# number = int(input("Input any ol' number! "))

# if number % 2 == 0 :
#     print(number , "is Even.")
# else: 
#     print(number , "is Odd.")



print("\n\n Example 2: \n\n\n")


# Programs will check if a person is eligable to vote 

age = 17

if age >= 18: 
    print("Yes, you can vote. Go, frolic in the wonders of poltics.")
else: 
    print("Nuh uh uh, no you don't.")


print("\n\nExample 3:\n ")

# Program to check if login credentials are correct 

username = input("Enter your username: ")#"admin"
password = input("Please enter your password: ")#"password123"

if username == "admin" and password == "password123":
    print("Login Successful: Please Proceed with grading.")
else:
    print("You are NOT authroized to use this system. >:(.")

print ("\n\n\n Example 4: \n")

grade = int(input("Please enter Eva's Grade for the test: "))

if grade >= 90: 
    print("Eva got an A on the test.") 
elif grade >= 80: 
    print("Eva got an B on the test.") 
elif grade >= 70: 
    print("Eva got a C on the test.")
elif grade >= 60: 
    print("Eva got a D on the test.")
else:
    print("Eva got an F on the test.")
