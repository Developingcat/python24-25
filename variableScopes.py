"""
Define a couple different types of variables in terms of their scope 
"""
import wedFunRetBellRinger
# Global Variable - 
global_var = "I am a global variable!! and I am accessible everywhere!!!"
name = "Hannah"
# Cannot use enclosing var out here, but it can be used WITHIN functions, as long as they are nested or the function
# They are defined within. 

def outer_function():
    # Enclosing scope variable
    enclosing_var = "I am an enclosing variable and accessible to nested functions!!!"
    
    def inner_function():
        # Local variables 
        local_var = "I am a local variable and only accessible within this function!!"


"""
local_var is only available inside of the inner_function Namespace 


enclosing_var is available inside of the outer_function Namespace and the inner_function Namespace 


global_var is available in all of the Namespaces created inside of this script, it would also be available inside of 
any script that imports the variableScopes.py scripts  
"""

# print(result) 

