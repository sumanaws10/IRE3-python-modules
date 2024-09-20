#print(5/0)
#print("The Program continue")

#################

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")
print("The program continues")