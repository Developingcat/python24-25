def sum(first,second): 
    total = first + second 
    return total 



def add_one(x):
    return x + 1 # This x variable is different 


# First step, call the sum 
result = sum(5,8)

print(result)

x = sum(10,20) # Different from this 

print(x) # Should be 30 if done correctly 

y = add_one(100)
print(y)


z = add_one(y) # This takes the result of the variable of y, so 101 being y's set value will become 102 due to the addition 
print(z)
