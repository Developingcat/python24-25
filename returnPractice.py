# Celsius to Fahrenheit 





def celsius_to_fahrenheit(celsius):

    """
    Summary
    Args: 
    celsius (float): Temperature in Celsius 

    return:
    float: Temperature in Fahrenheit 
    """
    return (celsius * 9/5 ) + 32 



def fahrenheit_to_celsius(fahrenheit):
    """
    Args: 
        fahrenheit (float): Temperature in Fahrenheit

    return: 
    float: Temperature in Celsius 
    
    """
    return (fahrenheit - 32) * 5/9



# Ask user what conversion they need to do. 
print("1. Convert celsius to fahrenheit")
print ("2. Convert fahrenheit to celsius")
choice = input("Enter your choice (1 or 2): ")



# Process the users choice

if choice == "1":
 celsius = float(input("Enter temperature in celsius: "))
 print(f"{celsius}*C is equal to {celsius_to_fahrenheit(celsius):.2f}*F")
elif choice == "2": 
    fahrenheit == float(input("Enter temperature in fahrenheit: "))
    print(f"{fahrenheit}*F is equal to {fahrenheit_to_celsius(celsius):.2f}*C")
else: 
    print("Invalid choice.") 