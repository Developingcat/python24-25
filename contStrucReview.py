"""
Booleans - Represent 2 possible values; True or False (1, 0 in Binary)
"""

print("\n\nExample of using Boolean values: \n")

isRaining = False
isSunny = True 

print(isRaining) # Output : False
print(isSunny) # Output : True 
print()

"""
Logical Operators: 

and - Returns True if both statements are true 
or - Returns True if one of the statements is true 
not - Reverses the Boolean value
"""


print("\nLogical Operators Examples: \n")

# 2 Variables

isWeekend = False 
isHoliday = False 


# Using and 

print(isWeekend and isHoliday) # Output - False 

# Using or 

print(isWeekend or isHoliday) # Output - False 

# Using not 
print(not isWeekend) # Output - True 

print(not isHoliday and isWeekend) #Output - False 

print(not isHoliday and not isWeekend) #Output - True 

print(not isWeekend or isHoliday) #Output - True 


"""
Comparison Operators: 
equal to : == 
not equal to : != 
greater then : >
less then : < 
greater then or euqal to : >= 
less then or equal to : <= 
"""

print("\n Example of Comparison Operators\n")

x = 10
y = 20 

print(x == y ) # Output False 
print ( x != y ) # Output True 
print ( x < y) # Output True 
print ( x >= y) # Output False


if x < y: 
    # code 
    print("This is the if code")
else: 
    #else code 
    print("This is the else code")


print()


"""
If Statement: Lets the program decide what code to run based on the condition 
"""

print("\nExample of an if statement")

num1 = 5 
num2 = 2 

if num2 > num1: 
    print("first if code block")
else: 
    print("first else code block")



if num1 ** num2 > 20: 
    print("second if code block")
else: 
    print("second else code block")

if num1 ** num2 != 25: 
    print("third if code block")
else: 
    print("third else code block")


print()

"""
Arithmetic Operators: 
+ : Addition 
- : Subtraction 
* : Multiplication 
** : Expnonet 
// : Floor Divison - before the decimal  
% : Modulus - after the decimal 
/ : Division 
"""


"""
for Loop - Used to iterate over a sequence (exp: a list or range of items)
Iteration - every time you repeat something is an itertion 
"""

print("\n in range for Loop Example:\n")
for i in range(5):
    print("Iteration:", i) # Output - Iteration and the number, will be off by one 



print("\nList Iteration for Loop Example\n")


myList = ["Gavin", "Hunter", "Hannah", "Connor", "Eva", "Christain"]

for i in myList:
    print(i)
    print(len(myList))


"""
While Loops - a loop that continues running as long as its condition is true 
BE CAREFUL OF INFINTE LOOPS 
"""

print("\nExample of a while Loop\n")


counter = 3 

while counter > 0: 
    print("Countdown:", counter)
    counter -= 1 
print("Blast Off!") 


print("\nExample two of a while Loop\n")

x = 5
y = 6
z = z = 5 * 6 # 30 

while True: 
    if z > 90:
        break
    else: 
        print(z)
        x = 10  
        y = 12
        z = x * y

print(z)
print()

