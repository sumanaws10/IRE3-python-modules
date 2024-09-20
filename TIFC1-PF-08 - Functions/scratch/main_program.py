#

# my_module.py
#def greet(name):
 #   print(f"Hello, {name}!")

# Import the entire module and call the function
import my_module
my_module.greet("Alice")  # Approach 1
 
# Import the function directly from the module
from my_module import greet
greet("Bob")  # Approach 2
 
# Import the function with an alias
from my_module import greet as gr
gr("Charlie")  # Approach 3
 
# Import the module with an alias and call the function
import my_module as mm
mm.greet("David")  # Approach 4
 
# Import everything from the module
from my_module import *
greet("Eve")  # Approach 5#