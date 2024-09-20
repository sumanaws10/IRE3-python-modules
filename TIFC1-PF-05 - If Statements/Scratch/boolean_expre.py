#Equal (==): Checks if two values are equal.

x = 10
if x == 10:
    print("x is equal to 10")
#Not Equal (!=): Checks if two values are not equal.
y = 5
if y != 10:
    print("y is not equal to 10")
#Greater Than (>): Checks if the value on the left is greater than the one on the right.
a = 15
if a > 10:
    print("a is greater than 10")
#Less Than (<): Checks if the value on the left is less than the one on the right.
b = 3
if b < 10:
    print("b is less than 10")
#Greater Than or Equal To (>=): Checks if the value on the left is greater than or equal to the one on the right.
c = 7
if c >= 5:
    print("c is greater than or equal to 5")
#Less Than or Equal To (<=): Checks if the value on the left is less than or equal to the one on the right.
d = 4
if d <= 4:
    print("d is less than or equal to 4")
#and: Combines two conditions and returns True only if both are true.
number = 15

if number > 10 and number < 20:
    print("The number is between 10 and 20.")
#or: Combines two conditions and returns True if at least one of them is true.
number = 3

if number < 5 or number > 100:
    print("The number is either less than 5 or greater than 100.")