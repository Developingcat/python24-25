"""
Program: counting.py 
author: Hannah O'Shea 
"""

print("Using the countine statement in a loop.")
print("------------------------------------")

currentNumber = 0

while currentNumber < 10:
    currentNumber += 1 # Control Variable 
    if currentNumber % 2 == 0: 
        continue
    print(currentNumber)