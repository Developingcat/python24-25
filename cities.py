"""
Program: cities.py 
Author: Hannah O'Shea

"""
print("Using a break statement to exit a loop.")
print("------------------------------------")

prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished)"

while True: 
    city = input(prompt)

    if city == 'quit':
        break 
    else:
       print(f"I'd love to go to {city.title()}!")

print("\n\nThank you for playing along.\n")