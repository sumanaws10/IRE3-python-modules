import module1


import module_name from module_name
import function_name from module_name i
import function_name as fn 
import module_name as mn
from module_name import *
####################
from module1 import function1 as f1

f1('argument1', 'argument2')
####################
import my_module as mm
result = mm.add(5, 3)
print(result)  # Output: 8

from my_module import greet as custom_greet

greeting = custom_greet("Alice")
print(greeting)  # Output: Hello, Alice!